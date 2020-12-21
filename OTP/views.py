from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.models import User

from .models import Profile
import random

import http.client

from django.conf import settings
from django.contrib.auth import authenticate, login

from OTP.process import caculate
# from django
# Create your views here.

def getOTP(request):
    ma=caculate.makecode()
    print(ma)
    return render(request, 'get_otp.html', {'ma':ma})

def verifyOTP(request):
    return render(request,'verify_otp.html')


