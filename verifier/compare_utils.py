
import re
from difflib import SequenceMatcher
from fuzzywuzzy import process, fuzz
from nltk import ngrams

# Returns if best match matches above specified ratio.
def compare_text(expected, ocr, threshold=98):
    if expected == '' or ocr == '':
        return False

    len_expected = len(expected.split())
    ngrams_list = list(ngrams(ocr.split(), len_expected))
    best_match = process.extractOne(expected,ngrams_list    , scorer=fuzz.token_sort_ratio)
    return best_match[1]  >= threshold

# Returns best match in ocr to expected string.
def extract_text(expected, ocr, threshold=98):
    if expected == '' or ocr == '':
        return ''

    len_expected = len(expected.split())
    ngrams_list = list(ngrams(ocr.split(), len_expected))
    best_match = process.extractOne(expected, ngrams_list, scorer=fuzz.token_sort_ratio)
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
