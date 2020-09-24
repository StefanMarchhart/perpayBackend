from django.contrib.auth.models import  Group
from api.models import PerpayUser
from rest_framework import viewsets
from api.serializers import UserSerializer, GroupSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import *



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



@api_view()
def ReturnTotals(request):
    return Response({
        "totalPaid":25235343.30,
        "totalPayments":521345,
        "totalUsers":50000,
        "totalCompanies":3000
    })


# @api_view()
# def ReturnTotals(request):
#     return Response({
#         "totalPaid":Payment.objects.aggregate(models.Sum('amount'))['amount__sum'],
#         "totalPayments":Payment.objects.all().count(),
#         "totalUsers":PerpayUser.objects.all().count(),
#         "totalCompanies":Company.objects.all().count()
#     })


