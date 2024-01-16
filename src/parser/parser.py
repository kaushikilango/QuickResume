import os
import spacy
import pprint
from spacy.matcher import Matcher
from ..entity_extraction import * as extractor

class ResumeParser(object):
    def __init__(self,resume):
        nlp = spacy.load('en_core_web_lg')
        self.__matcher = Matcher(nlp.vocab)
        self.__details__ = {
            'name' : None,
            'email': None,
            'mobile_number': None,
            'skills': None,
            'education': None,
            'experience': None,
        }
        self.__resume__ = resume
        self.__text_raw = extract_text_from_doc(self.__resume__,os.path.splitext(self.__resume__)[1])
        self.__text = nlp(self.__text_raw)
        self.__noun_chunks = list(self.__text.noun_chunks)
        self.__get_basic_details()
    
    def get_extracted_data(self):
        return self.__details__
    
    def __get_basic_details(self):
        name = extractor.extract_name(self.__text,self.__matcher)
        email = extractor.extract_email(self.__text)
        mobile_number = extractor.extract_mobile_number(self.__text,self.__noun_chunks)
        skills = extractor.extract_skills(self.__text)
        experience = extractor.extract_experience(self.__text)
        education = extractor.extract_education(self.__text)
        self.__details__['name'] = name
        self.__details__['email'] = email
        self.__details__['mobile_number'] = mobile_number
        self.__details__['skills'] = skills
        self.__details__['experience'] = experience
        self.__details__['education'] = education
        return

def resume_result_wrapper(resume):
    parser = ResumeParser(resume)
    return parser.get_extracted_data()
