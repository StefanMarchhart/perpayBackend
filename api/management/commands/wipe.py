from django.core.management.base import BaseCommand, CommandError
from api.models import PerpayUser,Company, Payment
from django.contrib.auth import get_user_model
import random

class Command(BaseCommand):
    help = 'Wipes all users and companies and payments from the db'

    def handle(self, *args, **options):

        Payment.objects.all().delete()
        PerpayUser.objects.all().delete()
        Company.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Successfully created Nuked everything'))
