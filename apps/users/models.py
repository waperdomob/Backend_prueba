from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.db import models
from django.forms import model_to_dict


class userRole(models.Model):
    role = models.CharField(max_length=45)

    def __str__(self):
        return self.role

class UserManager(BaseUserManager):
    def _create_user(self, username,first_name, email, password, is_staff, is_superuser, **extra_fields):
        user = self.model(
            username = username,
            first_name = first_name,
            email = email,
            is_staff = is_staff,
            is_superuser = is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, username, first_name, email,  password=None, **extra_fields):
        return self._create_user(username, first_name, email,  password, False, False, **extra_fields)

    def create_superuser(self, username,first_name, email, password=None, **extra_fields):
        return self._create_user(username,first_name, email,  password, True, True, **extra_fields)

class User(AbstractBaseUser , PermissionsMixin):

    username = models.CharField(max_length = 255, unique = True)
    first_name = models.CharField('Nombre', max_length = 255, blank = True, null = True)
    last_name = models.CharField('Apellido', max_length = 255, blank = True, null = True)
    email = models.EmailField('Correo Electrónico',max_length = 255, unique = True)
    is_superuser = models.BooleanField(default = False)
    is_staff = models.BooleanField(default = False)
    is_active = models.BooleanField(default = True) 
    date_joined= models.DateTimeField('fecha de registro', auto_now_add= True)
    date_update = models.DateTimeField('fecha de actualizacion', auto_now= True)
    role = models.ForeignKey(userRole, blank=True, null=True, on_delete=models.CASCADE)
    objects = UserManager()
    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name','email']


    def toJSON(self):
        item = model_to_dict(self, exclude=['password', 'user_permissions', 'last_login'])
        if self.last_login:
            item['last_login'] = self.last_login.strftime('%Y-%m-%d')
        item['date_joined'] = self.date_joined.strftime('%Y-%m-%d')
        item['date_update'] = self.date_update.strftime('%Y-%m-%d')
        item['groups'] = [{'id': g.id, 'name': g.name} for g in self.groups.all()]
        return item

    def natural_key(self):
        return (self.username)

    def __str__(self):
        return f'{self.first_name}'
