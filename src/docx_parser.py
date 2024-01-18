import docx 

def convert_to_string(doc):
    full_text = []
    document = docx.Document(doc)
    for paragraph in document.paragraphs:
        full_text.append(paragraph.text)
    return '\n'.join(full_text)


