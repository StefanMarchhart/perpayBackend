from django.core.management.base import BaseCommand, CommandError
from api.models import PerpayUser,Company, Payment
from django.contrib.auth import get_user_model
import random

class Command(BaseCommand):
    help = 'Sets up the database with some basic users/companies'

    def handle(self, *args, **options):

        # company = Company.objects.get_or_create("AdminCompany")
        if len(Company.objects.all()) ==0:
            company = Company.create("AdminCompany")

            user=get_user_model()
            user = PerpayUser.objects.create_superuser(username="admin",email="admin@admin.com",password="password",company=company.id)
            

            for i in range(1,random.randrange(1,10)):
                Payment.create(random.randrange(1,5000),user)

            self.stdout.write(self.style.SUCCESS('Successfully created Admin user and Company'))
        else:
            self.stdout.write(self.style.SUCCESS('Skipped initial setup'))


