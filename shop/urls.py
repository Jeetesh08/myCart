from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path("" , views.index , name = "Shop index"),
    path("about/" , views.about , name = "AboutUs"),
    path("contact/" , views.contact , name = "ContactUs"),
    path("tracker/" , views.tracker , name = "trackingStatis"),
    path("search/" , views.search , name = "search"),
    path("productview/" , views.productview , name = "productview"),
    path("checkout/" , views.checkout , name = "checkout"),








]