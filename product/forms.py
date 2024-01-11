from django import forms
from .models import Product, ProductImage 
# from multiupload.fields import MultiFileField



# class CustomProductForm(forms.ModelForm):
#     carousel_items = MultiFileField(min_num=1, max_num=10, required=False)
#     carousel_items_mob = MultiFileField(min_num=1, max_num=10, required=False)
#     interior_items = MultiFileField(min_num=1, max_num=10, required=False)
#     interior_items_mob = MultiFileField(min_num=1, max_num=10, required=False)

#     class Meta:
#         model = Product
#         fields = '__all__'

#     def save(self, commit=True):
#         product = super().save(commit=False)
#         if commit:
#             product.save()
#         for file in self.cleaned_data['carousel_items']:
#             image = ProductImage(product=product)
#             image.image = file
#             image.save()
#         for file in self.cleaned_data['carousel_items_mob']:
#             image = ProductImage(product=product)
#             image.image = file
#             image.save()
#         return product





# class CustomProductForm(forms.ModelForm):
#     carousel_items = MultiFileField(min_num=1, max_num=10, required=False)
#     carousel_items_mob = MultiFileField(min_num=1, max_num=10, required=False)

#     interior_items = MultiFileField(min_num=1, max_num=10, required=False)
#     interior_items_mob = MultiFileField(min_num=1, max_num=10, required=False)

#     class Meta:
#         model = Product
#         fields = '__all__'


#     def save(self, commit=True):
#         product = super().save(commit=False)
        
#         if commit:
#             product.save()

#         for file in self.cleaned_data['carousel_items']:
#             image = ProductImage(product=product, image=file)
#             image.save()
#         for file in self.cleaned_data['carousel_items_mob']:
#             image = ProductImage(product=product, image=file)
#             image.save()
#         for file in self.cleaned_data['interior_items']:
#             image = ProductImage(product=product, image=file)
#             image.save()
#         for file in self.cleaned_data['interior_items_mob']:
#             image = ProductImage(product=product, image=file)
#             image.save()

#         return product




    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     if self.instance.product_slug:
    #         self.fields['carousel_items'].initial = self.instance.carousel_items.all()

    # def save(self, commit=True):
    #     product = super().save(commit=False)
    #     if commit:
    #         product.save()
    #     if self.cleaned_data.get('carousel_items'):
    #         for image in self.cleaned_data['carousel_items']:
    #             ProductImage.objects.create(image=image, product=product)
    #     return product






# class ProductForm(forms.ModelForm):
#     class Meta:
#         model = Product
#         fields = ['product_full_name', 'carousel_items']
#         widgets = {
#             'carousel_items': forms.ClearableFileInput(attrs={
#                 'multiple': True}),
#         }

# class ProductImageForm(forms.ModelForm):
#     class Meta:
#         model = ProductImage
#         fields = ('image',)




# class ProductForm(forms.ModelForm):
#     carousel_items =  = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

#     class Meta:
#         model = Product
#         fields = ['product_full_name', 'fabric_name', 'price', 'price_sale', 'is_new', 'carousel_items']