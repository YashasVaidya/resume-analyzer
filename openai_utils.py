# openai_utils.py

import os
import openai

# Ensure the API key is set in the environment variable
if not os.getenv('OPENAI_API_KEY'):
    raise ValueError("Please set the OPENAI_API_KEY environment variable")

openai.api_key = os.getenv('OPENAI_API_KEY')

class OpenAIModel:
    def __init__(self, model_name="gpt-4o-mini"):
        self.model_name = model_name

    def generate(self, prompt):
        try:
            response = openai.ChatCompletion.create(
                model=self.model_name,
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=512,
                n=1,
                stop=None
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            print(f"Error with OpenAI API call: {e}")
            return "Error: Unable to process the request"
