from .models import Category, Collection, Color, Producttype, Option, Product

class FilterForm(forms.Form):
    collections = forms.ModelMultipleChoiceField(queryset=Collection.objects.all(), required=False)
    colors = forms.ModelMultipleChoiceField(queryset=Color.objects.all(), required=False)