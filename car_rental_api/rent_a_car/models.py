from django.db import models

# To Create A Custom User Model and admin panel
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.utils.translation import ugettext_lazy


# To Manage new users using this baseusermanaegr class
class MyuserManager(BaseUserManager):
    """ A Custom User Manager to deal with Emails  as an unique Identifier """

    def _create_user(self, email, username, password, **extra_fields):

        if not email:
            raise ValueError('Email Must Be Set')

        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password, **extra_fields):
        user = self._create_user(email, username, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, null=False)
    username = models.CharField(max_length=264)
    is_staff = models.BooleanField(
        default=False
    )
    is_active = models.BooleanField(
        default=True
    )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    objects = MyuserManager()

    class Meta:
        verbose_name_plural = 'User'
        db_table = 'User'

    def __str__(self):
        return self.email


def upload_image(instance, filename):
    return "cars/{filename}".format(filename=filename)
# Create your models here.


class Vehicles(models.Model):
    carName = models.CharField(max_length=264)
    carPicture = models.ImageField(upload_to=upload_image)
    carDescription = models.TextField(blank=True)
    carPrice = models.IntegerField(blank=True)
    capacity = models.IntegerField(blank=True, default=2)

    class Meta:
        verbose_name_plural = 'Vehicle'
        db_table = 'Vehicle'


    def __str__(self):
        return self.carName


class RentCar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vehicle = models.ManyToManyField(Vehicles)
    rent_from = models.DateTimeField(auto_now=True)
    rent_to = models.CharField(blank=True,max_length=264)


    class Meta:
        verbose_name_plural = 'Rent Car'
        db_table = 'Rent Car'

