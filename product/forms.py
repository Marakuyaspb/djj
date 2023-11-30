from django import forms
from .models import Product, ProductImage, FabricIconChange, Option







class ProductForm(forms.ModelForm):
    carousel_items =  = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

    class Meta:
        model = Product
        fields = ['product_full_name', 'fabric_name', 'price', 'price_sale', 'is_new', 'carousel_items']



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