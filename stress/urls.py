from django.urls import path
from . import views






urlpatterns = [
    path('',views.new_1,name='new_1'),
    path('about_us',views.about_us,name='about_us'),
    path('clickme',views.click_here,name='clickme'),
    path('data',views.data,name='data')

]

