from django import forms
from .models import Movie, Comment

class MovieForm(forms.ModelForm):
    GENRE_CHOICES = [
        ('', 'Choose a genre'), 
        ('comedy', 'Comedy'),
        ('horror', 'Horror'),
        ('action', 'Action'),
        ('thriller', 'Thriller'),
        ('sf', 'Science Fiction'),
        ('melo', 'Melodrama'),
    ]

    SCORE_CHOICES = [(x/2, f"{x/2}") for x in range(0, 11)] 

    genre = forms.ChoiceField(choices=GENRE_CHOICES, widget=forms.Select, required=True)
    score = forms.DecimalField(max_value=5, min_value=0, decimal_places=1, widget=forms.NumberInput(attrs={'step': '0.5'}))


    class Meta:
        model = Movie
        fields = ('title', 'description', 'genre', 'score')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
