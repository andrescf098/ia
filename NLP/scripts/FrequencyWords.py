import nltk
import re
from urllib import request
from bs4 import BeautifulSoup
from nltk.tokenize import word_tokenize


def get_freq_words(url, n, long = 1):
    req = request.urlopen(url)
    html = req.read().decode('utf8')
    raw = BeautifulSoup(html, 'html.parser')
    text = raw.get_text()
    tokens = re.findall(r'''(?x)(?:[A-Z]\.)+| \w+(?:-\w+)*| \$?\d+(?:\.\d+)?%?| \.\.\.| [][.,;"'?():-_`]''', text)
    toknes = [t.lower() for t in tokens]
    fd = nltk.FreqDist(tokens)
    return [t for (t, _) in fd.most_common(n) if len(t) >= long]