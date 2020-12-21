from .views import *
from django.urls import path,include

urlpatterns = [

    path('get-otp/' , getOTP, name="getOTP" ),
    path('', verifyOTP,  name="verifyOTP"),
    path('pass/' , success , name="pass"),
    path('fail/' , fail , name="fail"),
    # path('login-otp', login_otp , name="login_otp")     
    
]