from .views import *
from django.urls import path
urlpatterns = [
    path('',home),
    path('login/',login_page),
    path('addshop/',addshop),
    path('postshop/',postshop),
    path('nearshops/',nearshops),
    path('search/',search,name='search'),
    path('review/<uuid:pk>/',review)

]
