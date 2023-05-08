from django.shortcuts import render
from .serializer import *
from rest_framework.decorators import APIView , api_view , permission_classes
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated 
from rest_framework_simplejwt.tokens import RefreshToken , AccessToken
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import make_password
# Create your views here.

def get_access_token(user):
    token = RefreshToken.for_user(user=user)
    access_token = str(token.access_token)
    
    return ({
        'refresh_token': token,
        'access_token' : access_token
    })


import datetime
class Login(APIView):
    def post(self,request):
        email = request.data['email']
        password = request.data['password']
        user = authenticate(email = email,password = password)
        print(user)
        if user:
            token = get_access_token(user)
            access_token =token['access_token']
            refresh_token = token['refresh_token']
            user_time = CustomUser.objects.get(email = email)
            user_time.last_login = datetime.datetime.now()
            user_time.save()
            data  = {"user":str(user),
                     'merchant':str(user_time.is_shop),
                     "refresh_token":str(refresh_token),
                     'access_token':str(access_token),
                     'status':200}
            return Response(data,status=200)
        return Response('not_valid_Data',status = status.HTTP_406_NOT_ACCEPTABLE)


class User_registrations_view(APIView):
    def post(self,request):
        try:
            data = request.data
            user = CustomUser.objects.filter(email = data['email'])
            merchant = data['merchant']
            if user:
                userData = {'status':406,
                            'msg':'Email already registered'}
                return Response(userData,status = status.HTTP_406_NOT_ACCEPTABLE)
            serializer = User_profile_serializer(data = data)
            if serializer.is_valid():
                print(merchant)
                if (merchant)=='True' or (merchant)==True:
                    print(data['merchant'])
                    user = CustomUser.objects.create(email = data['email'],password = make_password(data['password']),is_shop=True)
                else:
                    print(data['merchant'],'merhcant')
                    user = CustomUser.objects.create(email = data['email'],password = make_password(data['password']))
                userData = get_access_token(user)
                access_token = userData['access_token']
                userData = {'access_token':access_token,
                            'merchant':user.is_shop,
                            'status':200}
                serializer.save()
                return Response(userData,status=status.HTTP_200_OK)
            userdata = {'status':406,
                        'msg':serializer.errors}
            return Response(serializer.errors,status=status.HTTP_406_NOT_ACCEPTABLE)
        except Exception as e:
            userdata = {'status':406,
                        'msg':str(e)}
            return Response(userdata,status=status.HTTP_400_BAD_REQUEST)
        
def register(request):
    return render(request , 'register.html')


class User_register(APIView):
    def post(self,request):
        try:
            data = request.data
            user_email = CustomUser.objects.get(email = data['email'])
            if user_email:
                serializer = User_profile_serializer(data = data)
                if serializer.is_valid():
                    serializer.save()
                    user = CustomUser.objects.create(email = data['email'],password = make_password(data['password']))
                    token = get_access_token(user)
                    access_token = token['access_token']
                    refresh_token = token['refresh_token']
                    userDataToken = {'user':str(user),
                                     'refresh_token':str(refresh_token),
                                     'access_token':str(access_token),
                                     'status':200}
                    return Response(userDataToken,status=status.HTTP_200_OK)
                return Response(serializer.errors,status=status.HTTP_406_NOT_ACCEPTABLE)
        except Exception as e:
            response_data = str(e)
            print(e)
            return Response(response_data,status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def usertoken(request):
    try:
        email = request.data['email']
        try:
            data = CustomUser.objects.get(email = email)
            token = get_access_token(data)
            access_token =token['access_token']
            refresh_token = token['refresh_token']
            data  = {"user":str(email),
                     'merchant':str(data.is_shop),
                     "refresh_token":str(refresh_token),
                     'access_token':str(access_token),
                     'status':200}
            return Response(data,status=200)
        except Exception as e:
            return Response({'status':406,'msg':f'Error {str(e)}'})
    except Exception as e:
        return Response({'status':406,'msg':f'Error Found : {str(e)}'})
        
