
from django.shortcuts import render, redirect
import logging
from .forms import LabelForm
from .ocr_utils import extract_text_from_image
from .compare_utils import compare_text, compare_abv, extract_text, extract_abv
from .models import Verification
from django.http import HttpResponse

def base(request):
    return render(request, "verifier/base.html")

def upload(request):
    if request.method == "POST":

        form = LabelForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            img = form.cleaned_data['image']
            ocr = extract_text_from_image(img)

            # Best values found by ocr.
            ocr_values = {
                'brand_name': extract_text(form.cleaned_data['brand_name'], ocr),
                'class_type': extract_text(form.cleaned_data['class_type'], ocr),
                'abv': extract_abv(ocr),
                'net_contents': extract_text(form.cleaned_data['net_contents'], ocr),
                'govt_warning': extract_text('government warning', ocr.lower())
            }

            # Dict of booleans for each field. True if these is a match, otherwise false.
            results = {
                'brand_name': compare_text(form.cleaned_data['brand_name'].lower(), ocr.lower()),
                'class_type': compare_text(form.cleaned_data['class_type'].lower(), ocr.lower()),
                'abv': compare_abv(form.cleaned_data['abv'].lower(), ocr),
                'net_contents': compare_text(form.cleaned_data.get('net_contents','').lower(), ocr.lower()),
                'govt_warning': 'government warning' in ocr.lower()
            }

            passed = all(results.values())

            return render(request, "verifier/result.html", {
                "ocr_text": ocr,
                "results": results,
                "overall_pass": passed,
                "form": form.cleaned_data,
                "ocr_values": ocr_values,
                'image': img
            })
    else:
        form = LabelForm()

    return render(request, "verifier/result.html", {"form": form})

