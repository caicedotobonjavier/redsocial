from typing import Any
from django.shortcuts import render
#
from django.views.generic import ListView, DetailView, TemplateView
#
from applications.posts.models import Post
#
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'home/index.html'
    login_url = 'users_app:login_user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        usuario = self.request.user
        context["user"] = usuario
        context["posts"] = Post.objects.all().order_by('-created')
        return context
    