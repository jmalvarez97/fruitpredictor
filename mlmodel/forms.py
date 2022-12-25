from django import forms
foods = ["apple","asparagus","banana","blackberry","broccoli","grapes","onion","pineapple","strawberry","watermelon"]

choices = (
    ('apple', 'Manzana'),
    ('asparagus', 'Esparrago'),
    ('banana', 'Banana'),
    ('broccoli' , 'Brocoli'),
    ('onion', 'Cebolla'),
    ('pineapple' , 'Anana'),
    ('strawberry' , 'Frutilla'),
    ('watermelon' , 'Sandia')
)
class UploadFileForm(forms.Form):
    name = forms.CharField(max_length=50, label="Fruta" )
    image = forms.ImageField()

class DrawFruit(forms.Form):
    name = forms.ChoiceField(choices=choices)
    metadata = forms.CharField(widget=forms.HiddenInput())