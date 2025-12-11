
import re
from difflib import SequenceMatcher

def normalize(s):
    return re.sub(r'[^a-z0-9% .-]', '', s.lower())

def fuzzy(a,b):
    return SequenceMatcher(None, normalize(a), normalize(b)).ratio()

def compare_text(expected, ocr, threshold=0.7):
    best = 0

    for part in ocr.split():
        sc = fuzzy(expected, part)
        best = max(best, sc)
        print(part, sc, best)
    return best >= threshold

def extract_text(expected, ocr, threshold=0.7):
    best = 0
    best_part = ''
    for part in ocr.split():
        sc = fuzzy(expected, part)
        if sc > best:
            best = max(best, sc)
            best_part = part
    return best_part

def extract_abv(ocr):
    abv = re.findall(r'(\d+(?:\.\d+)?)%', ocr)
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
