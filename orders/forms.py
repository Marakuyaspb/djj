from django import forms
from .models import Order

class OrderCreateForm(forms.ModelForm):
	class Meta:
		model = Order
		fields = ['first_name', 'city', 'phone', 'email']


	def __init__(self, *args, **kwargs):
		super(OrderCreateForm, self).__init__(*args, **kwargs)
		self.fields['first_name'].error_messages = {'required': 'custom required message'}

		# if you want to do it to all of them
		for field in self.fields.values():
			field.error_messages = {'required':'The field {fieldname} is required'.format(
                fieldname=field.label)}


		# error_messages = {
        #     'first_name': {
        #         'required': 'Custom error message for the first name field',
        #     },
        #     'city': {
        #         'required': 'Custom error message for the city field',
        #     },
        #     'phone': {
        #         'required': 'Custom error message for the phone field',
        #     },
        #     'email': {
        #         'required': 'Custom error message for the email field',
        #     },
        # }