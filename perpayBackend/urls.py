from django.contrib import admin
from django.urls import path
from django.urls import include, path
from rest_framework import routers
from api import views
from django.conf.urls import include
from rest_framework.authtoken.views import obtain_auth_token


router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('signup/', views.SignupView.as_view(), name="Signup" ),
    path('totals/', views.TotalsView.as_view(), name="Return Totals" ),
    path('testtotals/', views.TestTotalsView.as_view(), name="Return Totals with a Test Dataset" ),
    path('breakdown/', views.BreakdownView.as_view(), name="Return Breakdown of companies" ),
    path('testbreakdown/', views.TestBreakdownView.as_view(), name="Return Breakdown with a Test Dataset" ),
    path('companies/', views.CompaniesView.as_view(), name="Return a list of companies" ),
    path('setup/', views.SetupView.as_view(), name="Creates initial account" ),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]


