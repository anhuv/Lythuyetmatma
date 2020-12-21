from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.models import User


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
    if request.method == 'POST':
        otp = request.POST.get('otp')
        code= str(caculate.makecode())
        if otp == code:
            return redirect('pass')
        else:
            return redirect('fail')
    return render(request,'verify_otp.html')

def success(request):
    return render(request,'pass.html')

def fail(request):
    return render(request,'fail.html')
