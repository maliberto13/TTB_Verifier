
import re
from difflib import SequenceMatcher
from fuzzywuzzy import process, fuzz
from nltk import ngrams

def normalize(s):
    return re.sub(r'[^a-z0-9% .-]', '', s.lower())

def fuzzy(a,b):
    return process.extractOne(a,b,scorer=fuzz.ratio,)

def compare_text(expected, ocr, threshold=90):
    best = ''
    len_expected = len(expected.split())
    ngrams_list = list(ngrams(ocr.split(), len_expected))
    best_match = process.extractOne(expected,ngrams_list    , scorer=fuzz.token_sort_ratio)
    return best_match[1]  >= threshold

def extract_text(expected, ocr, threshold=90):
    best = ''
    len_expected = len(expected.split())
    ngrams_list = list(ngrams(ocr.split(), len_expected))
    print(expected)
    print('ngrams', ngrams_list)
    best_match = process.extractOne(expected, ngrams_list, scorer=fuzz.token_sort_ratio)
    print(best_match)
    return ' '.join(best_match[0])

def extract_abv(ocr):
    abv = re.findall(r'(\d+(?:\.\d+)?)%', ocr)
    if not abv:
        return ''
    return abv

def compare_abv(expected, ocr):
    m = re.search(r'(\d+(?:\.\d+)?)', expected)
    if not m: return False
    ev = float(m.group(1))
    found = extract_abv(ocr)
    for f in found:
        if abs(float(f)-ev) <= 0.3:
            return True
    return False
