#
from typing import Any
from django import forms
#
from .models import User
#
from django.contrib.auth import authenticate
#
from django.contrib.auth.hashers import check_password


class UserForm(forms.ModelForm):

    password1 = forms.CharField(
        required=True,
        label='Contraseña',
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Contraseña',
            }
        )
    )
    
    password2 = forms.CharField(
        required=True,
        label='Confirmar Contraseña',
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Confirmar contraseña',
            }
        )        
    )

    class Meta:
        model = User
        fields = (
            'email',
            'full_name',
            'phone',
            'address',
            'avatar',
            'date_birth',
        )

        widgets = {
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Correo electrónico',
                }
            ),
            'full_name': forms.TextInput(
                attrs={
                    'placeholder': 'Nombre completo',
                }
            ),
            'phone': forms.TextInput(
                attrs={
                    'placeholder': 'Teléfono',
                }
            ),
            'address': forms.TextInput(
                attrs={
                    'placeholder': 'Dirección',
                }
            ),
            'date_birth': forms.DateInput(
                attrs={
                    'type': 'date',
                }
            ),
        }
    
    def clean_password2(self):
        password2 = self.cleaned_data['password2']
        if password2 != self.cleaned_data['password1']:
            raise forms.ValidationError('Las contraseñas no coinciden')
        
        return password2



class ActivateAcountForm(forms.Form):
    codigo = forms.CharField(
        required=True,
        label='Código de activación',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Código de activación',
            }
        )
    )

    def __init__(self, pk, *args, **kwargs):     
        self.user = pk
        super(ActivateAcountForm, self).__init__(*args, **kwargs)
    

    def clean_codigo(self):
        id_user = self.user
        codigo = self.cleaned_data['codigo']
        user = User.objects.get(user_id=id_user)
        if user.cod_active != codigo:
            raise forms.ValidationError('Código de activación incorrecto')
        
        return codigo



class LoginForm(forms.Form):
    email = forms.EmailField(
        required=True,
        label='Correo Electronico',
        widget=forms.EmailInput(
            attrs={
                'placeholder': 'Correo electrónico',
            }
        )
    )

    password = forms.CharField(
        required=True,
        label='Contraseña',
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Contraseña',
            }
        )
    )
    
    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        email = cleaned_data['email']
        password = cleaned_data['password']

        user = authenticate(email=email, password=password)
        if not user:
            raise forms.ValidationError('Correo electrónico o contraseña incorrectos')
        
        return self.cleaned_data


class VerifyAcountForm(forms.Form):
    codigo = forms.CharField(
        required=True,
        label='Código de acceso',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Código de acceso',
            }
        )
    )

    def __init__(self, pk, *args, **kwargs):     
        self.user = pk
        super(VerifyAcountForm, self).__init__(*args, **kwargs)
    

    def clean_codigo(self):
        id_user = self.user
        codigo = self.cleaned_data['codigo']
        user = User.objects.get(user_id=id_user)

        if not check_password(codigo, user.login_otp):
            raise forms.ValidationError('Código de acceso incorrecto')

        if user.user_login_otp == True:
            raise forms.ValidationError('El código expiro, debe iniciar sesion nuevamente para obtener un nuevo codigo')
        
        return codigo