from django.urls import path, re_path, include
#
from . import views

app_name = 'home_app'


urlpatterns = [
    path('home/', views.IndexView.as_view(), name='home'),
]
