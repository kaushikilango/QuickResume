from openai import OpenAI
import os
def get_resume_details(resume_text):
    prompt = f"Given this resume:\n{resume_text}\n\nget details in this format: \n{{Name:..., experience: [...], education:[]}}"
    client = OpenAI(api_key = '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')
    responses = client.chat.completions.create(model = 'gpt-3.5-turbo',messages = [{'role':'user','content':prompt}])
    return responses.choices[0].message.content
