import re

def get_text(filepath):
    text = open(filepath, encoding="utf8").read()
    text = re.sub(r'<.*?>', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text