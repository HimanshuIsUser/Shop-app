from django.shortcuts import render
from .models import *
from login.models import *
from login.serializer import *
from rest_framework.decorators import APIView , api_view , permission_classes
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from geopy.distance import great_circle
from django.db.models import Q 
# Create your views here.

def home(request):
    data = Shop_profile.objects.all().values()
    return render(request,'index.html',{'data':data})

def login_page(request):
    return render(request,'login.html')

def profile(request):
    return render(request,'merchant_profile.html')

def addshop(request):
    return render(request,'addshop.html')

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def postshop(request):
    try:
        image = request.FILES.get('image')
        name = request.POST.get('shop_name')
        email = request.POST.get('shop_email')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        lat = request.POST.get('lat')
        lng = request.POST.get('lng')
        pincode = request.POST.get('pincode')
        number = request.POST.get('number')
        country = request.POST.get('country')
        user_email = request.POST.get('useremail')
        user_data = CustomUser.objects.get(email = user_email)
        try:
            new_shop = Shop_profile.objects.create(shop_name = name,shop_email = email,address = address,state = state , city= city, pincode = pincode,lat = lat,lng=lng,owner=user_data,shop_image = image,country=country,shop_mobile_no=number)
            return Response({'status':200,'msg':'Done'})
        except Exception as e:
            return Response({'status':406,'msg':f'Error Found : {str(e)}'})
    except Exception as e:
        print(e)
        return Response({'status':406,
                         'msg':f'Error {str(e)}'})



def nearshops(request):
    return render(request,'nearshops.html')



def distancefunc(set1,set2):
    distance = great_circle(set1,set2).kilometers
    if distance<10:
        return True
    else:
        return False


def search(request):
    word = request.GET.get('search')
    data = Shop_profile.objects.filter(Q(shop_name__icontains = word) | Q(city=word) | Q(address = word) | Q(country=word) | Q(pincode = word) | Q(state = word)).values()
    return render(request , 'nearshops.html',{'data':data})

@csrf_exempt
def review(request,pk=None):
    if request.method=='POST':
        word = request.POST.get('title')
        description = request.POST.get('description')
        shop = Shop_profile.objects.get(id = pk)
        if shop:
            review = Review.objects.create(shop = shop,description = description,title=word)
            data2 = Shop_profile.objects.filter(id=pk).values()
            all = Review.objects.filter(shop=shop)
            return render(request,'review.html',{'data':all,'owner':data2})
    else:
        owner = Shop_profile.objects.filter(id = pk).values()
        data = Review.objects.filter(shop = pk).values()
        return render(request,'review.html',{'owner':owner,'data':data})
