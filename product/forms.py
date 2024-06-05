from .models import Collection, Color, Producttype, Option, Product

class FilterForm(forms.Form):
    pass
    # collections = forms.ModelMultipleChoiceField(queryset=Collection.objects.all(), required=False)
    # colors = forms.ModelMultipleChoiceField(queryset=Color.objects.all(), required=False)