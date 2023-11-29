from django import forms
from .models import Product, FabricIconChange, Option


class ProductForm(forms.Form):
    pass

    # options = forms.ModelMultipleChoiceField(queryset=Option.objects.all(), widget=forms.CheckboxSelectMultiple)

    # product_fabric_icon = forms.ModelMultipleChoiceField(
    #     widget=forms.CheckboxSelectMultiple,
    #     queryset=FabricIconChange.objects.all()
    #     )

    # class Meta:
    #     model = Product
    #     fields = ['product_full_name', 'product_fabric_icon', 'options']



class FabricIconForm(forms.ModelForm):
    pass

    # class Meta:
    #     model = FabricIconChange
    #     fields = '__all__'
    #     widgets = {
    #         'product_fabric_icon': forms.ClearableFileInput(),
    #     }


class OptionForm(forms.ModelForm):
    pass

    # class Meta:
    #     model = Option
    #     fields = ['option_name', 'option_1_img', 'option_1_description', 'option_2_img', 'option_2_description']