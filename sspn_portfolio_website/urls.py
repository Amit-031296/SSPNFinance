from django.contrib import admin
from django.urls import path, include
from sspn_portfolio_website import views

app_name = 'sspn_portfolio_website'

urlpatterns = [

path("home/" , views.home, name="index"),

path("product_list/" , views.product_list, name="product_list"),

path("microfinance/" , views.microfinance, name="microfinance"),

path("homeloan/" , views.homeloan, name="homeloan"),

path("instantsalary/" , views.instantsalary, name="instantsalary"),

path("consumerfinance/" , views.consumerfinance, name="consumerfinance"),

path("aboutus/" , views.about_us, name="about_us"),

path("contactus/" , views.contact_us, name="contact_us"),

path("bloglist/" , views.blog_list, name="blog_list"),

path("blog/" , views.blog_detail, name="blog_detail"),

path("career/" , views.career, name="career"),

path("getconnected/" , views.signup_registration, name="signup_registration"),

path("getconnected/details" , views.detailed_registration, name="detailed_registration"),

]