from django.db import models
import datetime
from django.contrib.auth.models import AbstractUser
# from django.db import models
# from pygments.lexers import get_all_lexers
# from pygments.styles import get_all_styles

# LEXERS = [item for item in get_all_lexers() if item[1]]
# LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
# STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])


# class Snippet(models.Model):
#     created = models.DateTimeField(auto_now_add=True)
#     title = models.CharField(max_length=100, blank=True, default='')
#     code = models.TextField()
#     linenos = models.BooleanField(default=False)
#     language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
#     style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)

#     class Meta:
#         ordering = ['created']

# # Create your models here.






class Company(models.Model):
    name = models.CharField(max_length=100, verbose_name="Company Name")
    def __str__(self):
      return self.name


class PerpayUser(AbstractUser):
    Company= models.ForeignKey(Company, on_delete=models.CASCADE, null=True)





class Payment(models.Model):
    amount = models.DecimalField(max_digits=20, decimal_places=2, verbose_name="Payment Amount")
    date = models.DateField(verbose_name="Date of Payment")
    user = models.ForeignKey(PerpayUser, on_delete=models.CASCADE)
    def __str__(self):
      return "$"+str(self.amount)

