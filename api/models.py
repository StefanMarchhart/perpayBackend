from django.db import models
import datetime
from django.contrib.auth.models import AbstractUser, User,BaseUserManager
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class Company(models.Model):
    name = models.CharField(max_length=100, verbose_name="Company Name")
    def __str__(self):
      return self.name


class PerpayUserManager(BaseUserManager):
    def create_user(self,username,email,password=None,**extra_fields):
        print("Creating a new User")
        company=extra_fields.get("company")
        print(username,email,company,password)
        if not email:
            raise ValueError("User must have an email")
        if not password:
            raise ValueError("User must have a password")
        if not username:
            raise ValueError("User must have a Username")
        if not company:
            raise ValueError("User must have a company")
        
        user= self.model(
            email=self.normalize_email(email)
        )
        user.username = username
        user.company = Company.objects.get(id=company)or company
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,username,company,password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            username,
            company,
            password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class PerpayUser(AbstractUser):
    objects = PerpayUserManager()
    company= models.ForeignKey(Company, on_delete=models.CASCADE, null=True)

    REQUIRED_FIELDS = ['email','company' ]


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
        print("Token Created")




class Payment(models.Model):
    amount = models.DecimalField(max_digits=20, decimal_places=2, verbose_name="Payment Amount")
    date = models.DateField(verbose_name="Date of Payment")
    user = models.ForeignKey(PerpayUser, on_delete=models.CASCADE)
    def __str__(self):
      return self.user.username+"- $"+str(self.amount)

