from django.urls import path, re_path, include
#
from . import views

app_name = 'post_app'


urlpatterns = [
    path('new-post/', views.NewPostView.as_view(), name='new_post'),
]
