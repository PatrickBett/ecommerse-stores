from django.shortcuts import render, redirect

# Create your views here.
def admission(request):
	return render(request,'admission.html')


def contacts(request):
	return render(request,'contacts.html')
