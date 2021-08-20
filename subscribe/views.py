from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from .models import Product
from django.db.models import Q 
from django.urls import reverse
from django.core.mail import send_mail
from django.conf import settings



# Create your views here.
class ShopView(ListView):
	model = Product
	template_name = 'shop.html'

class EmailSuccessView(TemplateView):
	model = Product
	template_name = 'emailsuccess.html'



class SearchResultView(ListView):
	model = Product
	template_name = 'searchresult.html'
	context_object_name = 'searchlist'




#THIS FUNCTION PERFORMS SEaRCHING

	def get_queryset(self):
	    query = self.request.GET.get('q')
	    
	    return Product.objects.filter( Q(product__icontains=query) | Q(price__icontains=query) )



class PurchasesView(ListView):
	model=Product
	template_name='purchases.html'


def mail(request):
	if request.method=='POST':

		subject=request.POST.get('name')
		message=request.POST.get('message')
		from_email=request.POST.get('email')
		to_email=settings.EMAIL_HOST_USER

		send_mail(subject,message,from_email,[to_email], fail_silently=False)

		print("Email sent successfully")
		return render(request,'emailsuccess.html')
	return render(request,'shop.html')





	





