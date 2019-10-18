#<----imported libraries ------>
#django admin
from django.contrib import admin

#path,include,re_path
from django.urls import path, include,re_path

#</----imported libraries ------>

#<----- importing view ------>
from sspn_portfolio_website import views
#</----- importing view ------>

#<--- 
#defining App Name in Urls.py File
app_name = 'sspn_portfolio_website'
#---/>

urlpatterns = [
#<--- Pages Urls --->

#home page url
path("" , views.home, name="index"),

#<---product page url --->
#product page url
path("product_list/" , views.product_list, name="product_list"),

#on product page--microfinance page url
re_path(r'^microfinance/(?P<product_name>\w+)/$', views.microfinance, name="microfinance"),

#on product page--homeloan page url
path("homeloan/" , views.homeloan, name="homeloan"),

#on product page--instantsalary page url
re_path(r'^instantsalary/(?P<product_name>\w+)/$', views.instantsalary, name="instantsalary"),

#on product page--consumerfinance page url
re_path(r'^consumerfinance/(?P<product_name>\w+)/$', views.consumerfinance, name="consumerfinance"),

#</---product page url --->

#aboutus page url
path("aboutus/" , views.about_us, name="about_us"),

#contactus page url
path("contactus/" , views.contact_us, name="contact_us"),

#contactussuccess page url
path("contact_us_success/",views.contact_us_success,name="contact_us_success"),

#bloglist page url
path("bloglist/" , views.blog_list, name="blog_list"),

#blog page url
path("blog/" , views.blog_detail, name="blog_detail"),

#career page url
path("career/" , views.career, name="career"),

#microfinance,instantsalary,consumerfinance getconnected register page url
re_path(r'^getconnected/(?P<product_name>\w+)/$' , views.signup_registration, name="signup_registration"),

#detailed registration page url
path("getconnected/details/<int:pk>" , views.detailed_registration, name="detailed_registration"),

#</--- Pages Urls --->

#------ All Form Submit Processing URL -----------
#contactus form submit url
path("contact_us_submit/",views.contact_us_submit,name="contact_us_submit"),

#detailed registration form submit url
path("detailed_registration_submit/<int:pk>" , views.detailed_registration_submit, name="detailed_registration_submit"),

#signup registeration form submit url
re_path(r'^signup_registeration_form_submit/(?P<product_name>\w+)/$' , views.signup_registeration_form_submit, name="signup_registeration_form_submit")
#</------ All Form Submit Processing URL ----------- 
]