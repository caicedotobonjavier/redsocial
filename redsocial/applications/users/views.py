from django.shortcuts import render
#
from .forms import UserForm, ActivateAcountForm, LoginForm, VerifyAcountForm
#
from .models import User
#
from applications.posts.models import Post
#
from django.contrib.auth.mixins import LoginRequiredMixin
#
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView, View, TemplateView
#
from .functions import generate_code, send_mail_register, send_mail_verify
#
from django.urls import reverse_lazy, reverse
#
from django.http import HttpResponseRedirect
#
from datetime import datetime, timezone
#
import pyotp
#
from django.contrib.auth import authenticate, login, logout
#
from django.contrib.auth.hashers import make_password


class CreateUserView(FormView):
    form_class = UserForm
    template_name = 'users/create_user.html'
    success_url = reverse_lazy('users_app:activate_user')
    

    def form_valid(self, form):
        telefono = form.cleaned_data['phone']
        direccion = form.cleaned_data['address']
        nacimiento = form.cleaned_data['date_birth']
        foto = form.cleaned_data['avatar']
        codigo_otp = pyotp.random_base32()
        codigo = generate_code()

        user = User.objects.create_user(
            form.cleaned_data['email'],
            form.cleaned_data['full_name'],
            form.cleaned_data['password1'],
            address=direccion,
            date_birth=nacimiento,
            phone=telefono,
            avatar=foto,
            otp_base32 = codigo_otp,
            cod_active = codigo
        )

        url = user.user_id

        send_mail_register(form.cleaned_data['email'], form.cleaned_data['full_name'], codigo, url)

        return HttpResponseRedirect(
            reverse(                
                    'users_app:activate_user',
                    kwargs={'pk':user.user_id}               
            )
        )  



class ActivateUserView(FormView):
    form_class = ActivateAcountForm
    template_name = 'users/activate_acount.html'
    success_url = reverse_lazy('users_app:login_user')

    def get_form_kwargs(self):
        kwargs = super(ActivateUserView, self).get_form_kwargs()
        kwargs.update({'pk': self.kwargs['pk']})
        return kwargs

    def form_valid(self, form):
        user_activate = self.kwargs.get('pk')
        user = User.objects.get(user_id=user_activate)
        user.is_active = True
        user.save()

        return super(ActivateUserView, self).form_valid(form)


class LoginUserView(FormView):
    form_class = LoginForm
    template_name = 'users/login.html'
    success_url = '.'

    def form_valid(self, form):
        correo = form.cleaned_data['email']
        contrasena = form.cleaned_data['password']

        user = authenticate(email=correo, password=contrasena)
        otp_base32 = user.otp_base32
        totp = pyotp.TOTP(otp_base32).now()
        print(totp)
        user.login_otp = make_password(totp)
        user.created_at = datetime.now(timezone.utc)
        user.user_login_otp = False
        user.save(update_fields=['login_otp', 'created_at', 'user_login_otp'])   

        send_mail_verify(form.cleaned_data['email'], totp, user.user_id)


        return HttpResponseRedirect(
            reverse(
                'users_app:verify_user',
                kwargs={'pk': user.user_id}
            )
        )


class VerifyUserView(FormView):
    form_class = VerifyAcountForm
    template_name = 'users/verify_acount.html'
    success_url = reverse_lazy('home_app:home')

    def get_form_kwargs(self):
        kwargs = super(VerifyUserView, self).get_form_kwargs()
        kwargs.update({'pk': self.kwargs['pk']})
        return kwargs


    def form_valid(self, form):
        dato_user = self.kwargs['pk']
        user = User.objects.get(user_id=dato_user)
        user.user_login_otp = True
        user.save(update_fields=['user_login_otp'])

        login(self.request, user)

        return super(VerifyUserView, self).form_valid(form)



class LogoutView(View):

    def get(self, request, *args, **kwargs):
        logout(request)

        return HttpResponseRedirect(
            reverse(
                'users_app:login_user'
            )
        )


class PerfilUserView(LoginRequiredMixin, TemplateView):
    template_name = 'users/perfil_user.html'
    login_url = 'users_app:login_user'


    def get_context_data(self, **kwargs):
        context = super(PerfilUserView, self).get_context_data(**kwargs)
        usuario = self.request.user
        context["user"] = usuario
        context["posts"] = Post.objects.filter(user__id = usuario.id).order_by('-created')
        return context
    