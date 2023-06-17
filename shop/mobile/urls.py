from django.urls import path
from . import views


urlpatterns = [
    path('iphone/', views.MobileList.as_view() , name='mobile_list'),
    path('iphone/<int:pk>/', views.MobileDetail.as_view() , name='mobile_detail')
]
