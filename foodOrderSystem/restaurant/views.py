from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from restaurant.models import restaurantUser,foodItems
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate,login,logout,get_user_model
# Create your views here.


def loginRestaurant(request):
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password')
        
        # if not User.objects.filter(email = username).exists():
        #     messages.error(request,'Username is not in database')
        #     return redirect('login')

        user = authenticate(username=username, password=password)
   
        if user is None:
            messages.error(request,'Invalid Password or Username')
            return redirect('loginRestaurant')

        elif user.is_restaurant==False:
            messages.error(request,'You are a User')
            return redirect('loginRestaurant')
        else:
            login(request,user)
            messages.success(request,'Successfully Login')
            render(request,'loginRestaurant.html')
            return redirect('addMenu')


    return render(request,'loginRestaurant.html')


def registerRestaurant(request):
    if request.method == 'POST':
        
        restaurantName = request.POST.get('restaurantName')
        address = request.POST.get('address')
        restaurantContact = request.POST.get('restaurantContact')
        email = request.POST.get('email')
        password = request.POST.get('password')
        restaurant_data = restaurantUser(restaurantName=restaurantName,
                                     address=address,
                                     restaurantContact=restaurantContact,
                                     email=email,
                                     username=email,
                                     is_restaurant = True,
                                     password=make_password(password))
        
        if restaurantUser.objects.filter(email=email).exists() and restaurantUser.objects.filter(is_restaurant=True):
            messages.error(request,'User Already Exist in the System')
            return redirect('loginRestaurant')
        
        elif restaurantUser.objects.filter(email=email).exists() and restaurantUser.objects.filter(is_restaurant=False):
            messages.error(request,'You have Customer Account Using This Email ID. Try Another Email ID')
            return redirect('loginRestaurant')

        else:
            restaurant_data.save()
            messages.success(request,"Successfully Registered")
            return redirect('loginRestaurant')

    return render(request,'registerRestaurant.html')

@login_required
def addMenu(request):
    context = {}
    if request.user.is_restaurant:
        if request.user.is_authenticated:
            r = restaurantUser.objects.get(email=request.user)
            restaurant = r.restaurantName


        if request.method == 'POST':
            name = request.POST.get('name')
            price = request.POST.get('price')
            image = request.FILES.get('image')

            try:
                item = foodItems(name=name, price=price, image=image, restaurantName= restaurant )
                item.save()
                messages.success(request,"Successfully Added the Item")
            
            except:
                messages.error(request,'Error in adding Food Item')
     
        
        item = foodItems.objects.all()
        print(item)
        print(restaurant)
        
        context = {
            'name': restaurant,
            'items': item,
        }

    else:
        messages.error(request,'Login in as Restaurant')
        return redirect('loginRestaurant')
    
   
    return render(request, 'addMenu.html',context)


def logoutRestaurant(request):
    user = get_user_model()
    logout(request)
    return redirect("feedback_form")