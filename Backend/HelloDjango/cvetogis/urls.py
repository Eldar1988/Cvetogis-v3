from django.urls import path
from . import views


urlpatterns = [
    path('home_products/', views.HomeProductsView.as_view()),
    path('', views.HomePageDataView.as_view()),

]