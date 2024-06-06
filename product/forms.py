from django import forms
from .models import Collection, Color, Producttype, Option, Product

class FilterForm(forms.Form):
    colors = forms.ModelMultipleChoiceField(queryset=Color.objects.all(), required=False)
    min_price = forms.IntegerField(min_value=0, max_value=300000, required=False)
    max_price = forms.IntegerField(min_value=0, max_value=300000, required=False)



    # collections = forms.ModelMultipleChoiceField(queryset=Collection.objects.all(), required=False)
    # colors = forms.ModelMultipleChoiceField(queryset=Color.objects.all(), required=False)
    # price = filter(min_price__gt, max_price__lt)

    #filter_products = forms.ChoiceField(choices=CATEGORY_CHOICES, label='Choise')