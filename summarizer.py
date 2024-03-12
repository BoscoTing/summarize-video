import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
OPENAI_API_KEY = os.getenv("opai_api_key")

class Summarizer:
    def __init__(self, model="gpt-3.5-turbo"):
        self.my_helper = OpenAI(api_key=OPENAI_API_KEY)
        self.model_name = model

    def read_text(self, file_path):
        helper = self.my_helper
        with open(file_path, 'r', encoding='utf-8') as txt:
            text_content = txt.readlines()[0]
            completion = helper.chat.completions.create(
                model=self.model_name,
                messages=[
                    {"role": "system", "content": 'You are a professional finance analyser. Please use "繁體中文(台灣)" as language to list 5 key point as summarization, better with quantitative description, base on the article below:'},
                    {"role": "user", "content": text_content}
                ]
            )
        print(completion.choices[0].message)
        return completion.choices[0].message