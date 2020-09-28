from django.contrib.auth.models import  Group
from api.models import PerpayUser
from rest_framework import viewsets, status
from api.serializers import PerpayUserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import *
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class SignupView(APIView):
    # permission_classes = (IsAuthenticated,)             # <-- And here
    # authentication_classes = (TokenAuthentication, SessionAuthentication)

    def post(self, request):


        print(request.data)
        serializer = PerpayUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            token=Token.objects.get(user=PerpayUser.objects.get(username=serializer.data["username"]).id)
            return Response({"token":str(token)}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @csrf_exempt
# def signup(request):
#     # if request.method == 'GET':
#     #     Response({"Needs to be a POST Request"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
#     if request.method == 'POST':
#         # form = UserCreationForm(request.POST)

#         # data = JSONParser().parse(request)

#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     else:
#         return Response({"Needs to be a POST Request"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


        
    #     if form.is_valid():
    #         form.save()
    #         username = form.cleaned_data.get('username')
    #         raw_password = form.cleaned_data.get('password1')
    #         user = authenticate(username=username, password=raw_password)
    #         login(request, user)
    #         return redirect('home')
    # else:
    #     form = UserCreationForm()
    # return render(request, 'signup.html', {'form': form})


# class UserViewSet(viewsets.ModelViewSet):
#     queryset = PerpayUser.objects.all()
    # serializer_class = PerpayUserSerializer

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
            output.append([company.id,company.name])
        return Response(output)



# user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
# user.last_name = 'Lennon