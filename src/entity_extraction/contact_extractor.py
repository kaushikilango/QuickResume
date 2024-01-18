import re
import yaml
import spacy
from spacy.matcher import Matcher

with open('config.yaml') as f:
    config = yaml.safe_load(f)

def extract_contact(text):
    email = re.findall("([^@|\s]+@[^@]+\.[^@|\s]+)", text)
    if email:
        try:
            email = email[0].split()[0].strip(';')
        except IndexError:
            email = None
    else:
        email = None
    phone = re.findall(re.compile(r'(?:(?:\+?([1-9]|[0-9][0-9]|[0-9][0-9][0-9])\s*(?:[.-]\s*)?)?(?:\(\s*([2-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9])\s*\)|([0-9][1-9]|[0-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9]))\s*(?:[.-]\s*)?)?([2-9]1[02-9]|[2-9][02-9]1|[2-9][02-9]{2})\s*(?:[.-]\s*)?([0-9]{4})(?:\s*(?:#|x\.?|ext\.?|extension)\s*(\d+))?'), text)
    if phone:
        number = ''.join(phone[0])
        if len(number) > 10:
            phone = '+' + number
        else:
            phone = number
    return email,phone

if __name__ == '__main__':
    nlp = spacy.load('en_core_web_lg')
    text = config['TEST']['text']
    doc = nlp(text)
    matcher = Matcher(nlp.vocab)
    email,phone = extract_contact(text)
    print(email,phone)
        