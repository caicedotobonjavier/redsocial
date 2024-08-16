from django.shortcuts import render
#
from .forms import PostForm
#
from .models import Post
#
from django.views.generic import FormView, View
#
from django.urls import reverse_lazy
# Create your views here.


class NewPostView(FormView):
    template_name = 'post/agregar_post.html'
    form_class = PostForm
    success_url = reverse_lazy('home_app:home')


    def form_valid(self, form):

        Post.objects.create(
            user = self.request.user,
            title = form.cleaned_data['title'],
            content = form.cleaned_data['content'],
            image = form.cleaned_data['image'],
        )
        
        return super(NewPostView, self).form_valid(form)
    