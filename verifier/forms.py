
from django import forms
from .models import Verification

class LabelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(LabelForm, self).__init__(*args, **kwargs)
        self.fields['govt_warning'].required = False
        self.fields['net_contents'].required = False

    class Meta:
        model = Verification
        fields = ['brand_name', 'class_type', 'abv', 'net_contents', 'govt_warning', 'image']
