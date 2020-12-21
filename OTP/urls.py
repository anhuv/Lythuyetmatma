from .views import *
from django.urls import path,include

urlpatterns = [

    path('get-otp/' , getOTP, name="getOTP" ),
    path('', verifyOTP,  name="verifyOTP"),
    # path('register' , register , name="register"),
    # path('otp' , otp , name="otp"),
    # path('login-otp', login_otp , name="login_otp")     
    
]