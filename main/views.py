from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User



@api_view(['POST'])
def Login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return JsonResponse({'success':True})
        
    else:
        return JsonResponse({'success':False})

@api_view(['POST'])
def createUser(request):
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    user = User.objects.create_user(username=username,
                                 email=email,
                                 password=password)

    user.save()
    return JsonResponse({'success':True})
    
    