from django import forms
from .models import Fabric, Product

class FabricChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return '<img src="%s" width="50" />' % obj.product_fabric_icon.url

    label_from_instance.allow_tags = True

class ProductForm(forms.ModelForm):
    fabric = FabricChoiceField(queryset=Fabric.objects.all())

    class Meta:
        model = Product
        fields = '__all__'