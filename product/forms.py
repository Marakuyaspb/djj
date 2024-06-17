from django import forms
from .models import Collection, Color, Producttype, Product

class FilterForm(forms.Form):
    collection = forms.ModelMultipleChoiceField(queryset=Collection.objects.all(), required=False)
    color_id = forms.ModelMultipleChoiceField(queryset=Color.objects.all(), required=False)
    type_id = forms.ModelMultipleChoiceField(queryset=Producttype.objects.all(), required=False)
    min_price = forms.IntegerField(min_value=0, max_value=300000, required=False)
    max_price = forms.IntegerField(min_value=0, max_value=300000, required=False)
    min_width = forms.IntegerField(min_value=30, max_value=400, required=False)
    max_width = forms.IntegerField(min_value=30, max_value=400, required=False)
    min_depth = forms.IntegerField(min_value=30, max_value=400, required=False)
    max_depth = forms.IntegerField(min_value=30, max_value=400, required=False)
    mechanism_type = forms.BooleanField(required=False)
    sleep_place = forms.BooleanField(required=False)
    linen_drawer = forms.BooleanField(required=False)