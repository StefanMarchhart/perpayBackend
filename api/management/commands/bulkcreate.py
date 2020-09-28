from django.core.management.base import BaseCommand, CommandError
from api.models import PerpayUser,Company, Payment
from django.contrib.auth import get_user_model
import random

class Command(BaseCommand):
    help = 'Sets up the database with some basic users/companies'

    def handle(self, *args, **options):
        if len(Company.objects.all())< 5:

            company_names=["charity", "grocery", "assignment", "industry", "negotiation", "mud", "performance", "committee", "patience", "meaning", "student", "teaching", "message", "agency", "county", "inspector", "president", "fortune", "instruction", "television", "estate", "inflation", "refrigerator", "examination", "organization", "death", "teacher", "warning", "idea", "psychology", "establishment", "mode", "session", "politics", "analysis", "transportation", "difference", "variation", "version", "information", "addition", "dinner", "homework", "protection", "property", "writing", "hotel", "possession", "problem"]
            company_titles=["LLC", "Inc", "Co", "Corp", "Ltd"]
            names=["Jacob", "Michael", "Matthew", "Joshua", "Christopher", "Nicholas", "Andrew", "Joseph", "Daniel", "Tyler", "William", "Brandon", "Ryan", "John", "Zachary", "David", "Anthony", "James", "Justin", "Alexander", "Jonathan", "Christian", "Austin", "Dylan", "Ethan", "Benjamin", "Noah", "Samuel", "Robert", "Nathan", "Cameron", "Kevin", "Thomas", "Jose", "Hunter", "Jordan", "Kyle", "Caleb", "Jason", "Logan", "Aaron", "Eric", "Brian", "Gabriel", "Adam", "Jack", "Isaiah", "Juan", "Luis", "Connor"]
            last_names=["Smith", "Johnson", "Williams", "Brown", "Jones", "Miller", "Davis", "Garcia", "Rodriguez", "Wilson", "Martinez", "Anderson", "Taylor", "Thomas", "Hernandez", "Moore", "Martin", "Jackson", "Thompson", "White", "Lopez", "Lee", "Gonzalez", "Harris", "Clark", "Lewis", "Robinson", "Walker", "Perez", "Hall", "Young", "Allen", "Sanchez", "Wright", "King", "Scott", "Green", "Baker", "Adams", "Nelson", "Hill", "Ramirez", "Campbell", "Mitchell", "Roberts", "Carter", "Phillips", "Evans", "Turner", "Torres"]
            for index,company in enumerate(company_names):
                print("*****Creating users for : "+company+" - "+str(index)+" of "+str(len(company_names))+"*****")
                company = Company.create(company.capitalize()+" "+random.choice(company_titles))
                for name in range(1,random.randrange(1,20)):
                    fullname=names[name]+" "+random.choice(last_names) +" "+ str(random.randrange(1,9999))
                    user = PerpayUser.objects.create_user(username=fullname, email=fullname+"@gmail.com",password="password",company=company.id)
                    for i in range(1,random.randrange(1,20)):
                        Payment.create(random.randrange(1,5000),user)
            
        else:
            self.stdout.write(self.style.SUCCESS('Skipped Database fill'))


