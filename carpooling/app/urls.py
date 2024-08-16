from django.urls import path
from app.views import *

app_name = "app"
urlpatterns = [
    path('', base, name='base'),
    path('create/', create_userdetails, name='create_userdetails'),
    path('userdetail/', userdetails_list, name='userdetails_list'),
    path('accept/<int:userdetail_id>/', accept, name='accept'),
    path('reject/<int:userdetail_id>/', reject, name='reject'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('index/', index, name='index'),
    path('logout/',logout_view, name='logout'),
    path('sos/', sos, name='sos'),
    path('save-url/', save_url, name='save_url'),
    path('h/', h, name='h'),
    path('success/',success_url,name='success_url'),
    path('displayprice/<price>/', display_price, name='display_price'),
    path('pay/',pay,name='payment'),
    path('trip/', trip_form, name='trip_form'),
    path('tripsuccess/', trip_success, name='trip_success'),
]

