#<----imported libraries ------>
#django admin
from django.contrib import admin

#path,include,re_path
from django.urls import path, include,re_path

#</----imported libraries ------>

#<----- importing view ------>
from sspn_lead_manager_app import views
#</----- importing view ------>

#<--- 
#defining App Name in Urls.py File
app_name = 'sspn_lead_manager_app'
#---/>

urlpatterns = [
#<----- authentication URLs ------>
#Login page url
path("login/" , views.login, name="login"),

#Register page url
path("register/" , views.register, name="register"),

#ForgetPassword url
path("forget_password/" , views.forget_password, name="forget_password"),
#</----- authentication URLs ------>

#<--- Pages Urls --->
#Dashboard page url
path("index/" , views.home, name="index"),

#Leads collected Page url
path("leads_collected/" , views.leads_collected, name="leads_collected"),

#micro Finance Page Url
path("micro_finance/" , views.micro_finance, name="micro_finance"),

#home loan page Url
path("home_loan/" , views.home_loan, name="home_loan"),

#instant salary page url
path("instant_salary/" , views.instant_salary, name="instant_salary"),

#consumer finance page url
path("consumer_finance/" , views.consumer_finance, name="consumer_finance"),

#all status page url
path("all_status/" , views.all_status, name="all_status"),

#pending Status page url
path("pending_status/" , views.pending_status, name="pending_status"),

#In Process Status page url
path("in_process_status/" , views.in_process_status, name="in_process_status"),

#Approved Status page url
path("approved_status/" , views.approved_status, name="approved_status"),

#Rejected Status page url
path("rejected_status/" , views.rejected_status, name="rejected_status"),

#Team page url
path("team_sspn/" , views.team_sspn, name="team_sspn"),

#user Profile page url
path("user_profile/" , views.user_profile, name="user_profile"),

#Report error page url
path("report_error/" , views.report_error, name="report_error"),

#</--- Pages Urls --->

# <------ Django Bootstrap Modal Urls ------>
# <--- Lead CURD URLs ---
#AllLeads-update
path('update/<int:pk>',views.LeadUpdateView.as_view(), name='leads_update'),

#AllLeads-delete
path('delete/<int:pk>',views.LeadDeleteView.as_view(), name='leads_delete'),
# </--- Lead CURD URLs ---

# <--- Team CURD URLs ---
#Team-update
path('teamupdate/<int:pk>',views.TeamUpdateView.as_view(), name='teamupdate'),

#Team-delete
path('teamdelete/<int:pk>',views.TeamDeleteView.as_view(), name='teamdelete'),

#Team-create or add
path('add/new/team_member', views.add_new_teammember_view.as_view(), name='add_new_team_member'),
# </--- Team CURD URLs ---

# </------ Django Bootstrap Modal Urls ------>
]