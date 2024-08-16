from django.db import models
#
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
#
import uuid
#
from .managers import UserManager
# Create your models here.

class User(AbstractBaseUser, PermissionsMixin):
    user_id = models.UUIDField('Id usuario', default=uuid.uuid4, editable=False)
    email = models.EmailField('Correo electronico', unique=True)
    full_name = models.CharField('Nombre completo', max_length=100)
    phone = models.CharField('Telefono', max_length=15, blank=True, null=True)
    address = models.CharField('Direccion', max_length=50, blank=True, null=True)
    avatar = models.ImageField('Foto', upload_to='photo-perfil', blank=True, null=True)
    date_birth = models.DateField('Fecha nacimiento', blank=True, null=True)
    cod_active = models.CharField('Codigo Activacion', max_length=6, blank=True)
    #
    otp_base32 = models.CharField(max_length=225, blank=True, null=True)
    login_otp = models.CharField(max_length=255, blank=True, null=True)
    user_login_otp = models.BooleanField(default=False)
    created_at = models.DateTimeField('OTP creado', blank=True, null=True)
    #
    is_staff = models.BooleanField('Staff', default=False)
    is_active = models.BooleanField('Activo', default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name',]

    objects = UserManager()

    def get_email(self):
        return self.email
    

    def get_full_name(self):
        return self.full_name
