from django import forms
from Filmes.models import FilmeReview


class FilmeReviewModel(forms.ModelForm):
    class Meta:
        model = FilmeReview
        fields = '__all__'