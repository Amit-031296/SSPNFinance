from django.contrib import admin
from django.urls import path, include,re_path
from sspn_portfolio_website import views

app_name = 'sspn_portfolio_website'

urlpatterns = [

path("" , views.home, name="index"),

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

re_path(r'^getconnected/(?P<product_name>\w+)/$' , views.signup_registration, name="signup_registration"),

path("getconnected/details/<int:pk>" , views.detailed_registration, name="detailed_registration"),

path("detailed_registration_submit/<int:pk>" , views.detailed_registration_submit, name="detailed_registration_submit"),

re_path(r'^signup_registeration_form_submit/(?P<product_name>\w+)/$' , views.signup_registeration_form_submit, name="signup_registeration_form_submit")
]