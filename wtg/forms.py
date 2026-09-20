from django import forms


class PlaceForm(forms.Form):
    name = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea, required=False)
    kind = forms.CharField(max_length=50, required=False)
    location = forms.CharField(max_length=200, required=False)
    rating = forms.IntegerField(min_value=1, max_value=5)
