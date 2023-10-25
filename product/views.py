from django.shortcuts import render

def index(request):
	return render(request, 'product/index.html')

def about(request):
	return render(request, 'product/about.html')

def category_goods(request):
	return render(request, 'product/category_goods.html')

def contact(request):
	return render(request, 'product/contact.html')

def payment(request):
	return render(request, 'product/payment.html')

def showrooms(request):
	return render(request, 'product/showrooms.html')