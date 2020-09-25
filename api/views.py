from django.contrib.auth.models import  Group
from api.models import PerpayUser
from rest_framework import viewsets
from api.serializers import UserSerializer, GroupSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import *
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, TokenAuthentication


def validateRangeValue(value):
    # basic validation of get request
    if not value:
        return None
    
    if not value.isnumeric():
        return None

    return int(value)    



def FetchCompaniesInRange(start=0,end=20):
    return Company.objects.all().order_by("name")[start:end]


def FetchDataForCompany(company):
    paymentQS = Payment.objects.filter(user__company=company)
    usersQS = PerpayUser.objects.filter(company=company)

    users = usersQS.count() if usersQS.exists() else 0
    paid = paymentQS.aggregate(models.Sum('amount'))['amount__sum'] if paymentQS.exists() else 0
    count = paymentQS.count() if paymentQS.exists() else 0
    
    return {
        "company":company.name,
        "paid":paid,
        "payments":count,
        "users":users,

    }


class TotalsView(APIView):
    permission_classes = (IsAuthenticated,)             # <-- And here
    authentication_classes = (TokenAuthentication, SessionAuthentication)

    def get(self, request):
        content = {
            "totalPaid":Payment.objects.aggregate(models.Sum('amount'))['amount__sum'],
            "totalPayments":Payment.objects.all().count(),
            "totalUsers":PerpayUser.objects.all().count(),
            "totalCompanies":Company.objects.all().count()
        }
        return Response(content)

class TestTotalsView(APIView):
    permission_classes = (IsAuthenticated,)             # <-- And here
    authentication_classes = (TokenAuthentication, SessionAuthentication)

    def get(self, request):
        content = {
            "totalPaid":25235343.30,
            "totalPayments":521345,
            "totalUsers":50000,
            "totalCompanies":3000
        }
        return Response(content)


class BreakdownView(APIView):
    permission_classes = (IsAuthenticated,)             # <-- And here
    authentication_classes = (TokenAuthentication, SessionAuthentication)

    def get(self, request):

        start = validateRangeValue(request.query_params.get("start")) or 0
        end = validateRangeValue(request.query_params.get("end")) or 10
        output=[]
        for company in FetchCompaniesInRange(start,end):
            output.append(FetchDataForCompany(company))

        content = {
            "totalPaid":25235343.30,
            "totalPayments":521345,
            "totalUsers":50000,
            "totalCompanies":3000
        }
        return Response(output)


class TestBreakdownView(APIView):
    permission_classes = (IsAuthenticated,)             # <-- And here
    authentication_classes = (TokenAuthentication, SessionAuthentication)

    def get(self, request):
        output=[]
        for companyno in range(1,11):
            output.append({
                "company":"Company "+str(companyno),
                "paid":50000,
                "payments":20,
                "users":8,
            })
        return Response(output)



class CompaniesView(APIView):
    def get(self, request):
        output=[]
        for company in FetchCompaniesInRange(0,None):
            output.append(company.name)
        return Response(output)