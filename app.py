# app.py

from flask import Flask, render_template, request, redirect, url_for, flash
from openai_utils import OpenAIModel
import os
from io import BytesIO
from PyPDF2 import PdfReader

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secure key in production

# Initialize OpenAI model
openai_model = OpenAIModel("gpt-4o-mini")  # You can change the model if needed

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'resume' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['resume']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            # Read the PDF file content directly
            file_content = file.read()

            # Send the PDF content to OpenAI for processing
            work_analysis_result = analyze_work_experience(file_content)
            skills_result = classify_skills(file_content)

            return render_template('result.html', work_analysis=work_analysis_result, skills=skills_result)
    return render_template('index.html')

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'pdf'}

def extract_text_from_pdf(file_content):
    # Use PdfReader to read the PDF content
    reader = PdfReader(BytesIO(file_content))
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    print("Extracted Text:", text)  # Debug: Print extracted text
    return text

def analyze_work_experience(file_content):
    """
    Use OpenAI API to analyze work experience directly from PDF content.
    """
    # Extract text from PDF content
    text_content = extract_text_from_pdf(file_content)
    
    prompt = f"""
Analyze the work experience from the following text content and convert it into concise, impactful bullet points. Each bullet should be short and focus on key achievements or responsibilities. Each bullet should start with a '-'. Each bullet should be a single sentence. Each bullet should be at most 12 words. Use simple language and avoid unnecessary details.

Text Content:
{text_content}

Concise Bullet Points:
"""
    print("Prompt for Work Experience:", prompt)  # Debug: Print prompt
    result = openai_model.generate(prompt)
    print("OpenAI Response for Work Experience:", result)  # Debug: Print API response
    
    # Split the response into a list of bullet points, removing the leading dash
    work_experience_list = [line.strip()[1:].strip() for line in result.splitlines() if line.strip().startswith('-')]
    return work_experience_list

def classify_skills(file_content):
    """
    Use OpenAI API to classify skills directly from PDF content.
    """
    # Extract text from PDF content
    text_content = extract_text_from_pdf(file_content)
    
    prompt = f"""
Extract and classify the skills from the following text content into 'Technical Skills' and 'Soft Skills'. List each skill under the appropriate category, starting with 'Technical Skills:' and 'Soft Skills:'.

Text Content:
{text_content}

Skills Classification:
"""
    print("Prompt for Skills Classification:", prompt)  # Debug: Print prompt
    result = openai_model.generate(prompt)
    print("OpenAI Response for Skills Classification:", result)  # Debug: Print API response
    
    # Parse the response into a dictionary
    skills_dict = parse_skills_response(result)
    return skills_dict

def parse_skills_response(response):
    skills_dict = {"Technical Skills": [], "Soft Skills": []}
    current_category = None

    for line in response.splitlines():
        line = line.strip()
        if line.startswith("**Technical Skills:**"):
            current_category = "Technical Skills"
        elif line.startswith("**Soft Skills:**"):
            current_category = "Soft Skills"
        elif line.startswith("-") and current_category:
            skill = line[1:].strip()  # Remove the leading dash and strip whitespace
            skills_dict[current_category].append(skill)

    return skills_dict

if __name__ == '__main__':
    # Create uploads directory if it doesn't exist
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
    app.run(debug=True)
