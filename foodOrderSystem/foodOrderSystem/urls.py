"""
URL configuration for foodOrderSystem project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from customer import views as customerviews
from menu import views as menuviews
from order import views as orderviews
from restaurant import views as restaurantviews
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',customerviews.loginUser,name = 'login'),
    path('logout/',customerviews.logoutUser,name = 'logout'),
    path('logoutRestaurant/',restaurantviews.logoutRestaurant,name = 'logoutR'),
    path('register/',customerviews.registerUser,name = 'register'),
    path('forgetPassword/',customerviews.forgetPassword,name = 'forgetPassword'),
    path('menu/',menuviews.menu,name = 'menu'),
    path('loginRestaurant/',restaurantviews.loginRestaurant,name = 'loginRestaurant'),
    path('registerRestaurant/',restaurantviews.registerRestaurant,name = 'registerRestaurant'),
    path('feedback/', customerviews.feedback_form, name='feedback_form'),
    path('contact/', customerviews.index, name='index'),
    path('', customerviews.Home, name='Home'),
    path('addMenu/', restaurantviews.addMenu, name='addMenu'),
    path('cart/', orderviews.Cart, name='cart'),
    path('restaurantPage/', menuviews.restaurantPage, name='restaurantPage'),

    
    

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
