from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomePageDataView.as_view())
]