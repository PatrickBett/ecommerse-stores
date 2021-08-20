from django.shortcuts import render
from django.core.mail import send_mail
from django.views.generic import ListView
from accounts.models import user


# Create your views here.
#def sendmail(request):

#	subject = "Thankyou"
#	message = "Congratulations for creating an account on our organization"
#	EMAIL_HOST_USER = EMAIL_HOST_USER
#	recipient = {{user.email}}
#	send_mail(subject, message, EMAIL_HOST_USER, [recipient], fail_silently = False)


#	return render(request,'EmailList.html')


class EmailListView(ListView):
	model = user
	template_name = 'EmailList.html'