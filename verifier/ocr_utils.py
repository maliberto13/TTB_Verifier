
import re
from PIL import Image, ImageOps
import pytesseract
from django.conf import settings

def preprocess_image(img):
    g = img.convert("L")
    return ImageOps.autocontrast(g)

def extract_text_from_image(f):
    img = Image.open(f)
    img = preprocess_image(img)
    text = pytesseract.image_to_string(img, lang='eng')
    text = re.sub(r'\s+', ' ', text)
    return text
