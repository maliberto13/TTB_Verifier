
from django.db import models

class Verification(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    # form_data = models.JSONField()
    # extracted_text = models.TextField(blank=True)
    # result_summary = models.JSONField()
    brand_name = models.CharField(max_length=200)
    class_type = models.CharField(max_length=200)
    abv = models.CharField(max_length=50)
    net_contents = models.CharField(max_length=50, default="")
    govt_warning = models.BooleanField(default=False)
    image = models.ImageField()
    passed = models.BooleanField(default=False)

    def __str__(self):
        return f"Verification {self.id} - {'PASS' if self.passed else 'FAIL'}"
