import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import CountVectorizer
import docx
from nltk.corpus import wordnet as wn

def convert_to_string(doc):
    full_text = []
    document = docx.Document(doc)
    for paragraph in document.paragraphs:
        full_text.append(paragraph.text)
    return '\n'.join(full_text)

stop_words = set(stopwords.words('english'))
def remove_stopwords(text):
    words = text.split()

    filtered_words = [word for word in words if word not in stop_words]

    return ' '.join(filtered_words)

def vectorize_count(text):

    vectorizer = CountVectorizer()
    matrix = vectorizer.fit_transform(text)
    matrix = matrix.toarray().tolist()[0]
    features = vectorizer.get_feature_names_out()
    return dict(zip(features,matrix))

def tag_cleanse(tags):
    cleansed_tags = []
    for k in tags:
        t = []
        for i in wn.synsets(k):
            t.append(i.pos())
        x = sorted(i for i in t if t.count(i) > 2)
        if len(x) == 0 or x[0] != 'v':
            cleansed_tags.append(k)
    return cleansed_tags

def find_tags(counts):
    sorted_counts = sorted(counts.items(),key = lambda x:x[1])
    tags = []
    for x,k in sorted_counts[::-1]:
        tags.append(x)
    tags = tag_cleanse(tags)
    return tags[:20]

def extract_skills(text):
    filtered_text = remove_stopwords(text)
    counts = vectorize_count([filtered_text])
    tags = find_tags(counts)
    return tags

if __name__ == '__main__':
    doc = 'C:\Git\QuickResume\src\data\Resume00112101.docx'
    text = convert_to_string(doc)
    print(extract_skills(text))
