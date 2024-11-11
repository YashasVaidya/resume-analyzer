# Resume Analyzer

This project is a web application that analyzes resumes to extract work experience and classify skills using OpenAI's API. The application is built with Flask and processes PDF resumes.

## Prerequisites

- Python 3.7+
- [OpenAI API Key](https://beta.openai.com/signup/)
- [Flask](https://flask.palletsprojects.com/)
- [PyPDF2](https://pypi.org/project/PyPDF2/)

## Installation

1. **Clone the repository:**

   ```bash
   git clone <repository-url>
   cd resume-analyzer
   ```

2. **Set up a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set the OpenAI API Key:**

   Ensure your OpenAI API key is set in the environment variable `OPENAI_API_KEY`:

   ```bash
   export OPENAI_API_KEY='your_openai_api_key'  # On Windows use `set`
   ```

## Running the Application

1. **Start the Flask application:**

   ```bash
   python app.py
   ```

2. **Access the application:**

   Open your web browser and go to `http://127.0.0.1:5000/`.

3. **Upload a Resume:**

   - Use the web interface to upload a PDF resume.
   - The application will analyze the resume and display the results, including work experience and skills classification.

## Notes

- Ensure the `uploads` directory is created automatically when the application runs.
- Replace `your_secret_key` in `app.py` with a secure key for production use.

## Troubleshooting

- If you encounter issues with PDF reading, ensure the file is a valid PDF.
- Check the console for any error messages related to the OpenAI API.