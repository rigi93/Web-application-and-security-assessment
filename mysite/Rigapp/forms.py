from django import forms
from .models import uploadimg


class DocumentForm(forms.ModelForm):
    print ('form')
    usr_image = forms.ImageField()
#This ensures that the image file uploaded is off the form PNG, JPG or GIF
    description = forms.CharField(required=False)
# The required = false ensures that even if nothing is entered in the field still it gets validated
    class Meta:
        model = uploadimg
        fields = ('usr_image', 'description')