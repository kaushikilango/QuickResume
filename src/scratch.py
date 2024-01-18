from openai import OpenAI
import os
def get_resume_details(resume_text):
    prompt = f"Given this resume:\n{resume_text}\n\nget details in this format: \n{{Name:..., experience: ['company':...,'role':...,'period':...], education:['university':...,'degree':...,'period':...],skills:[]}} Dont add any other fields"
    client = OpenAI(api_key = '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')
    responses = client.chat.completions.create(model = 'gpt-3.5-turbo',messages = [{'role':'user','content':prompt}])
    return responses.choices[0].message.content
