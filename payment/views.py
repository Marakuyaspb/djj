from decimal import Decimal
from django.conf import settings
from django.shortcuts import render, redirect, reverse,\
get_object_or_404
from orders.models import Order


##описание метода в документации
#https://www.tinkoff.ru/kassa/develop/api/payments/init-description/

# Define the payment information as a dictionary
# Replace with your Tinkoff Merchant Terminal Key

#terminal_key = settings.TERMINALKEY

# Replace with your Tinkoff Merchant Secret Key

#secret_key = settings.TERMINALPASSWORD



def payment_process(request):
	order_id = request.session.get('order_id', None)
	order = get_object_or_404(Order, id=order_id)
	if request.method == 'POST':
		success_url = request.build_absolute_uri(reverse('payment:completed'))
		cancel_url = request.build_absolute_uri(reverse('payment:canceled'))

		session_data = {
			'mode': 'payment',
			'client_reference_id': order.id,
			'success_url': success_url,
			'cancel_url': cancel_url,
			'line_items': []
			}

		for item in order.items.all():
			session_data['line_items'].append({
				'price_data': {
				'unit_amount': int(item.price * Decimal('100')),
				'currency': 'usd',
				'product_data': {
					'name': item.product.name,
					},
				},
				'quantity': item.quantity,
			})


		return redirect(session.url, code=303)
	else:
		return render(request, 'payment/process.html', locals())


# TINKOFF EXAMPLE 

	# values = {
	# 	'Amount': str(cert.price*100)+'.00',#*100 потому что указывается сумма в копейках
	# 	'Description': str(cert.product.title)+' ('+str(cert.count)+') шт.', # The order description
	# 	'OrderId': str(cert.number_cert),
	# 	'Password': secret_key,
	# 	'TerminalKey': terminal_key
	# }
	# # Concatenate all values in the correct order
	# concatenated_values = ''.join([values[key] for key in (values.keys())])

	# # Calculate the hash using SHA-256 algorithm
	# hash_object = hashlib.sha256(concatenated_values.encode('utf-8'))
	# token = hash_object.hexdigest()
	# logger.debug('shop.views(1159) buy token {} ',token)

	# payment_data = {
	# 		'TerminalKey':terminal_key,
	# 		'OrderId': str(cert.number_cert),
	# 		'Amount': str(int(cert.price*100)),#*100 потому что указывается сумма в копейках
	# 		"Description": str(cert.product.title)+' ('+str(cert.count)+') шт.', # The order description
	# 		"Language": "ru", # The language code (ru or en)
	# 		"PayType": "O", # The payment type (O for one-time payment)
	# 		"Recurrent": "N", # Indicates whether the payment is recurrent (N for no)
	# 		# "CustomerKey": "1234567890", # The customer key (optional)

	# 		'Token':token,
	# 		'DATA': {
	# 				'Phone': cert.investor.phone,
	# 				'Email': cert.investor.email,
	# 		},
	# 		'PaymentMethod': {
	# 				'Type': 'Mobile',
	# 				'Data': {},
	# 		},
	# 		# данные чека
	# 		'Receipt': {
	# 				'Phone': str(cert.investor.phone),
	# 				'Email': str(cert.investor.email),
	# 				'Taxation':'usn_income',#упрощёнка
	# 				'Items':[{  #https://www.tinkoff.ru/kassa/develop/api/receipt/#Items
	# 						'Name':str(cert.product.title),
	# 						'Quantity':str(cert.count),
	# 						'Amount': str(int(cert.price*100)),
	# 						'Tax':'none',#без НДС
	# 						'Price':str(int(cert.product.price*100)),
	# 				},]
	# 				}, # your receipt data

	# 		# "SuccessURL": str(request.scheme+'://'+request.get_host()+"/youSuccess_path/?you_get="+str(your.pk)), # The URL for successful payments
	# 		# # "NotificationURL":request.scheme+'://'+request.get_host()+request.get_full_path()+'&CertId='+str(cert.pk), # The URL for payment notifications
	# 		# "FailURL":  str(request.scheme+'://'+request.get_host()+"/youFailURL_path/?you_get="+str(your.pk)), The URL for failed payments

	# 		}

	# #путь по которому мы отправляем свой запрос, прописан в документации банка
	# url = "https://securepay.tinkoff.ru/v2/payments/"

	# response = requests.post(url, json=payment_data)
	# logger.debug('shop.views Buy (1143) Tinkoff response {}',response.json())

	# if response.json()['Success']:
	# 		payment_url = response.json()['PaymentURL']

	# 		# Redirect the user to the payment form

	# 		Certificate.objects.filter(id=cert.id).update(PaymentId=response.json()['PaymentId'])

	# 		# отправляем пользователя на платёжную форму
	# 		return redirect(payment_url)
	# else:
	# 		# result = False
	# 		message = response.json()['Message']+' '+response.json()['Details']
	# 		messages.error(request, message)
	# 		logger.debug('shop.views(1191) buy response payment_url response {} ',response.json())




def payment_completed(request):
	return render(request, 'payment/completed.html')
def payment_canceled(request):
	return render(request, 'payment/canceled.html')