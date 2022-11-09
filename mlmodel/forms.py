from django import forms
class UploadFileForm(forms.Form):
    name = forms.CharField(max_length=50, label="Fruta" )
    image = forms.ImageField()

class DrawFruit(forms.Form):
    name = forms.CharField(max_length=50, label="Fruta")
    metadata = forms.CharField(widget=forms.HiddenInput())