from django.urls import path, re_path, include
#
from . import views

app_name = 'users_app'


urlpatterns = [
    path('create-new-user/', views.CreateUserView.as_view(), name='create_user'),
    path('activate-user/<pk>/', views.ActivateUserView.as_view(), name='activate_user'),
    path('login-user/', views.LoginUserView.as_view(), name='login_user'),
    path('verify-user/<pk>/', views.VerifyUserView.as_view(), name='verify_user'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('perfil-user/', views.PerfilUserView.as_view(), name='perfil'),
]
