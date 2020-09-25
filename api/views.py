from django.contrib.auth.models import  Group
from api.models import PerpayUser
from rest_framework import viewsets
from api.serializers import UserSerializer, GroupSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import *
import math



class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = PerpayUser.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class PaymentViewset(viewsets.ViewSet):

    print()

def validateRangeValue(value):
    # basic validation of get request
    if not value:
        return None
    
    if not value.isnumeric():
        return None

    return int(value)    



def SortByDollarsPaid(start=0,end=20):
    print("ahhh")

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

@api_view()
def TestTotals(request):
    return Response({
        "totalPaid":25235343.30,
        "totalPayments":521345,
        "totalUsers":50000,
        "totalCompanies":3000
    })


@api_view()
def ReturnTotals(request):
    return Response({
        "totalPaid":Payment.objects.aggregate(models.Sum('amount'))['amount__sum'],
        "totalPayments":Payment.objects.all().count(),
        "totalUsers":PerpayUser.objects.all().count(),
        "totalCompanies":Company.objects.all().count()
    })


@api_view()
def ReturnBreakdownInRange(request):
    
    start = validateRangeValue(request.query_params.get("start")) or 0
    end = validateRangeValue(request.query_params.get("end")) or 10
    output=[]
    for company in FetchCompaniesInRange(start,end):
        output.append(FetchDataForCompany(company))
    return Response(output)
    
@api_view()
def TestBreakdown(request):
    # start = validateRangeValue(request.query_params.get("start")) or 0
    # end = validateRangeValue(request.query_params.get("end")) or 10
    output=[]
    for companyno in range(1,11):
        output.append({
            "company":"Company "+str(companyno),
        "paid":50000,
        "payments":20,
        "users":8,
        })
    return Response(output)
    


