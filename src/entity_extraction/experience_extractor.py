from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import nltk
import yaml
import re
def extract_experience(text):
    wordnet_lemmatizer = WordNetLemmatizer()
    stop_words = set(stopwords.words('english'))
    word_tokens = nltk.word_tokenize(text)
    filtered_sentence = [w for w in word_tokens if not w in stop_words and wordnet_lemmatizer.lemmatize(w) not in stop_words] 
    sent = nltk.pos_tag(filtered_sentence)
    
    cp = nltk.RegexpParser('P: {<NNP|NN>+}')

    cs = cp.parse(sent)

    experiences = []
    for vp in list(cs.subtrees(filter=lambda x: x.label()=='P')):
        experience_text = " ".join([i[0] for i in vp.leaves() if i[1] in ['NNP', 'NN']])
        experiences.append(experience_text)

    return experiences

with open('config.yaml') as f:
    config = yaml.load(f, Loader=yaml.FullLoader)
