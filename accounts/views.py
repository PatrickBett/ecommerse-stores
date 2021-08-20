
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import user
from django.views.generic import ListView
from django.conf import settings




class DetailsView(ListView):
	model = user
	template_name = 'databaselist.html'


def register(request):


	if request.method=='POST':

		Firstname=request.POST['firstname']
		Lastname=request.POST['lastname']
		Email=request.POST['email']
		Username=request.POST['username']
		Password1=request.POST['password1']
		Password2=request.POST['password2']
		
		if Password1 == Password2:
			#user=User.objects.create_user(first_name=Firstname,last_name=Lastname,email=Email,password=Password1,username=Username)
			#user.save()
			


			if user.objects.filter(username = Username).exists():
				messages.success(request,'Username Taken')
				print("Username Taken")
			else:
			    user(firstname = Firstname,lastname = Lastname,username = Username,email = Email,password1 = Password1,password2 = Password2).save()
		
			
			    print ("successfull")


			    #def send_mail(request):
			    #	subject='Welcome to our platform'
			    #	message='Congratulations for engaging with our organization'
			    #	from_email=settings.EMAIL_HOST_USER
			    #	to_email=[user.email]

			    #	send_mail(subject,message,from_email,to_email,fail_silently=False)
			    #	print('Email sent successfully')
			    #	return render(request,'emailsent.html')

			    	

			    #sending emails
			    #sendemail(request)
			    #subject = "ThankYou for registering with our organization"
			    #message = "Congratulations for enrolling to the company, we are highly appreciating you"
			    #from_email = settings.EMAIL_HOST_USER
			    #to_email = [user.email]


			    #send_mail(subject,message,EMAIL_HOST_USER,to_email,fail_silently=False)
			    #print("Email sent successfully")


 
			    messages.success(request,'Registration successfull, You can now login')
			    return redirect("login")
		else :
			messages.error(request,'Passwords Not Matching')
			return render(request,'register.html')
	else:
		return render(request,'register.html')

	return render(request,'register.html')



#def sendmail(request):
#	subject='Welcome to our organization'
#	message='Congratulations you have successfully registered to our company. You are highly Welcomed'
#	from_email=settings.EMAIL_HOST_USER
#	to_email=[user.email]
#
#	send_mail(subject,message,from_email,to_email, fail_silently=False)

#	return render(request,'emailsent.html')






def login(request):

	if request.method=='POST':
		username=request.POST['username']
		password=request.POST['password1']

		user=auth.authenticate(username=username, password=password)

		if user is None:

			auth.login(request,user)

			print("You are logged in")

			return redirect('account')

		else :
			messages.warning(request,'Username Does not exist, you can Register')
			print("You are not logged in")
			return redirect('register')
		
	else :
	    return render(request,'login.html')
    

	return render(request,'login.html')

	

def logout(request):
	
	return render(request, 'login.html')


def password_reset(request):
	return render(request,'passwordresetform.html')


#def sendemail(request):
#	recipient =   
#	subject = "Registration successfull"
#	message = "Congratulations for joining the organization. ThankYou!"

#	send_mail(subject=subject, message=message, EMAIL_HOST_USER, recipient= recipient, fail_silently = False) 



def passwordreset(request):
	return render(request,'passwordresetform.html')


	    
def aboutus(request):
	return render(request,'aboutus.html')

def ict(request):
	return render(request,'Ict.html')
	
def plumbing(request):
	return render(request,'plumbing.html')

def Electrical(request):
	return render(request,'Electrical.html')

def hair_beauty(request):
	return render(request,'hair beauty and cosmetics.html')

def account(request):
	return render(request,'account.html')


	