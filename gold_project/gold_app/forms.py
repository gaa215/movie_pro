from django import forms
from . models import Movie
class MovieForm(forms.ModelForm):
    class Meta:
        model=Movie
        fields=['name','image','description','release_date','actors','category','trailer_link']

