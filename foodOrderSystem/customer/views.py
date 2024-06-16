from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from random import choice
from customer.models import customerUser, Feedback, Contact

from django.contrib.auth import get_user_model
# Create your views here.

User = get_user_model()

def loginUser(request):

    
    if request.method == 'POST':
        User = get_user_model()
        username = request.POST.get('email')
        password = request.POST.get('password')
        
        # if not User.objects.filter(email = username).exists():
        #     messages.error(request,'Username is not in database')
        #     return redirect('login')

        user = authenticate(username=username, password=password)
        print(user)
        if user is None:
            messages.error(request,'Invalid Password or Username')
            return redirect('login')
        elif user.is_restaurant:
            messages.error(request,'You are Registered as restaurant')
            return redirect('login')
        else:
            login(request,user)
            messages.success(request,'Successfully Login')
            render(request,'authentication/login.html')
            return redirect('menu')


        
    return render(request,'authentication/login.html')

def registerUser(request):
    if request.method == 'POST':
        
        User = get_user_model()
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if customerUser.objects.filter(email= email).exists():
            messages.error(request,'User Already Exist in the System')
            return redirect('login')
        hashed_password = make_password(password)


        try:
            user = customerUser.objects.create(
                name=name,
                email=email,
                username=email,
                password=hashed_password,
                is_user=True
            )
            user.save()
            messages.success(request,'Successfully Registered')
            return redirect('login')
        except:
            messages.error(request,'Error!! Try Again')
            

    return render(request,'authentication/register.html')

def forgetPassword(request):
    return render(request,'authentication/forgetPassword.html')

def logoutUser(request):
    User = get_user_model()
    logout(request)
    return render(request,'authentication/logout.html')

def feedback_form(request):

    if request.method == 'POST':
        print("entered")
        
        comments=request.POST.get('comment')
        try:
            Fb = Feedback() 
            Fb.stars = 0
            Fb.comments = comments
            Fb.save()
            return render(request, 'thank_you.html')  # Render the thank you page
        except:
            return HttpResponse('<h1>Sorry!</h1><p>There is an issue</p>')
    return render(request,'feedback.html')

def index(request):
    if request.method == "POST":
        contact = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        contact.name = name
        contact.email = email
        contact.subject = subject
        contact.save()
        return render(request, 'thank_you.html')  # Render the thank you page
    return render(request, 'contact.html')

def Home(request):
    return render(request,'home.html')
