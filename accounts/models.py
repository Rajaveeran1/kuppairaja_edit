
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.validators import RegexValidator

# Create your models here.
# don't usefull teble
class Role(models.Model):
    userrole = models.CharField(max_length=100)
    
  


class UserManager(BaseUserManager):
    def create_user(self, phone, password=None, is_staff=False, is_active=True, is_superuser=False):
        if not phone:
            raise ValueError('users must have a phone number')
        if not password:
            raise ValueError('user must have a password')

        user_obj = self.model(phone=phone)
        user_obj.set_password(password)
        user_obj.staff = is_staff
        user_obj.active = is_active
        user_obj.super = is_superuser
       

        user_obj.save(using=self._db)
        return user_obj

    def create_staffuser(self, phone, password=None):
        user = self.create_user(phone,password=password,is_staff=True,)
        return user

    def create_superuser(self, phone, password=None):
        user = self.create_user(
            phone,
            password=password,
            is_staff=True,
            is_superuser=True,
        )
        return user



class User(AbstractBaseUser):

   # userrole=(
      #  ('seller','SELLER'),
      # ('buyer','BUYER'),
      #  )
    
    userid= models.AutoField(primary_key=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Up to 15 digits allowed.")
    #userole = models.CharField(max_length=25,default="")
    userrole = models.ForeignKey(Role, on_delete=models.SET_NULL, blank=True, null=True, related_name='role')
    #userrole = models.ForeignKey(Role, on_delete=models.CASCADE, null=True, blank=True)
    phone = models.CharField(validators=[phone_regex], max_length=15, unique=True)
    business_name  = models.CharField(max_length=50, blank=True,)
    email=models.EmailField(blank=True, null=True)
    address = models.TextField(max_length=500, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    zipcode = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    image = models.ImageField(upload_to="images/", blank=True, null=True)
    first_login = models.BooleanField(default=False)
    otp = models.CharField(max_length=9, blank=True, null=True)
    verified = models.BooleanField(default=True, help_text='If otp verification got successful')
    count = models.IntegerField(default=0, help_text='Number of otp sent')
 
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    super = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
  
    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.phone

    def get_full_name(self):
        return self.fname + " " + self.lname

    def get_short_name(self):
        return self.phone

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):

        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_active(self):
        return self.active

    @property
    def is_superuser(self):
        return self.super
