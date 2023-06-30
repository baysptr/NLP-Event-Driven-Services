import nltk
from nltk.corpus import stopwords
import re
import string
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

# First Run after that can comment
nltk.download('punkt')
nltk.download('stopwords')

factory = StemmerFactory()
stemmer = factory.create_stemmer()

def removeStopwords(tokens):
    listStopword = set(stopwords.words('indonesian'))
    removed = []
    for t in tokens:
        if t not in listStopword:
            removed.append(t)
    return removed

def wordCloud(yourText):
    case_folding = yourText.lower()

    # jadikan kata dasar dan menghilangkan nomor - nomor
    case_folding = stemmer.stem(re.sub(r'\d+', '', case_folding))

    # hilangkan tanda baca
    case_folding = case_folding.translate(str.maketrans('', '', string.punctuation))

    # tokenisasi / pisah kata
    tokens = nltk.tokenize.word_tokenize(case_folding)

    # hitung text
    kemunculan = nltk.FreqDist(removeStopwords(tokens))
    words = kemunculan.most_common()
    respons = []
    for i in words:
        respons.append({'word': i[0], 'count': i[1]})
    return respons

# print(wordCloud("Jokowi kecewa kepada kapolri karena penanganan di kampung bandit tidak berjalan dengan baik"))