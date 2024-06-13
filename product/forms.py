from django import forms
from .models import Collection, Color, Producttype, Option, Product

class FilterForm(forms.Form):
    collections = forms.ModelMultipleChoiceField(queryset=Collection.objects.all(), required=False)
    colors = forms.ModelMultipleChoiceField(queryset=Color.objects.all(), required=False)
    producttypes = forms.ModelMultipleChoiceField(queryset=Color.objects.all(), required=False)

    min_price = forms.IntegerField(min_value=0, max_value=300000, required=False)
    max_price = forms.IntegerField(min_value=0, max_value=300000, required=False)
    width = forms.IntegerField(min_value=30, max_value=400, required=False)
    depth = forms.IntegerField(min_value=30, max_value=400, required=False)

    mechanism_type = forms.CharField(required=False)
    linen_drawer = forms.CharField(required=False)