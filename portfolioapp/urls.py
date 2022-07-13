from django.urls import path
from portfolioapp.views import * 

app_name = "portfolioapp"

urlpatterns = [
    path('', IndexView.as_view(), name = ''),
]
