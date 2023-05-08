from django.db import models
from django.contrib.auth.base_user import BaseUserManager , AbstractBaseUser
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import PermissionsMixin
import uuid
# Create your models here.


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, password=None, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)
    



    
class CustomUser(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(max_length=100, unique=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin=models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_shop = models.BooleanField(default = False)
     
        

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email    
    

class User_profile(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4 , editable=False)
    name = models.CharField(max_length=150, null=True,blank=True)
    email = models.EmailField(max_length=254, null=True,blank=True)
    mobile_no = models.CharField(max_length=50,null=True,blank=True)
    age = models.CharField(max_length=50,null=True,blank=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE , null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Shop_profile(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4 , editable=False)
    shop_image = models.ImageField(upload_to="")
    shop_name = models.CharField(max_length=150, null=True,blank=True)
    shop_email = models.EmailField(max_length=254, null=True,blank=True)
    shop_mobile_no = models.CharField(max_length=50,null=True,blank=True)
    lat = models.CharField(max_length=150,null=True,blank=True)
    lng = models.CharField(max_length=150,null=True,blank=True)
    address = models.CharField(max_length=250,null=True,blank=True)
    pincode = models.CharField(max_length=100,null=True,blank=True)
    state = models.CharField(max_length=100,null=True,blank=True)
    country= models.CharField(max_length=100,null=True,blank=True)
    city = models.CharField(max_length=100,null=True,blank=True)
    owner = models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True,blank=True)
    user_profile = models.ForeignKey(User_profile, on_delete=models.CASCADE , null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
class Review(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4 , editable=False)
    shop = models.ForeignKey(Shop_profile, on_delete=models.CASCADE,null=True,blank=True)
    title = models.CharField(max_length=150,null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)