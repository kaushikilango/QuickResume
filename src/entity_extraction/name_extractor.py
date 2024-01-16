import yaml
import spacy
from spacy.matcher import Matcher


with open('config.yaml') as f:
    config = yaml.safe_load(f)

def extract_name(text,matcher):
    """
    Extracts name from text using matcher
    """
    pattern = config['PATTERN']['NAME']
    matcher.add('NAME',[pattern])

    matches = matcher(text)

    for match_id, start, end in matches:
        span = text[start:end]
        return span.text