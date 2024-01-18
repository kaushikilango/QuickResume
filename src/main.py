from scratch import get_resume_details
from entity_extraction.experience_extractor import extract_experience
from entity_extraction.name_extractor import extract_name
from entity_extraction.contact_extractor import extract_contact
from docx_parser import convert_to_string
import spacy
from spacy.matcher import Matcher



def parse(doc):
    text = convert_to_string(doc)
    print("Loading English Module...")
    nlp = spacy.load('en_core_web_lg')
    print("English Module Loaded.")
    dc = nlp(text)
    matcher = Matcher(nlp.vocab)
    name = extract_name(dc,matcher)
    email, phone = extract_contact(text)
    experience = extract_experience(text)
    details = get_resume_details(text)
    return details,email,phone

if __name__ == '__main__':
    doc = 'C:\Git\QuickResume\src\data\Resume00112181.docx'
    details,email,phone = parse(doc)
    print(details)
    print(f'Email : {email}')
    print(f'Phone : {phone}')