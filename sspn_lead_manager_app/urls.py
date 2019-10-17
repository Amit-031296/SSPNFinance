from django.contrib import admin
from django.urls import path, include
from sspn_lead_manager_app import views

app_name = 'sspn_lead_manager_app'

urlpatterns = [

path("login/" , views.login, name="login"),

path("register/" , views.register, name="register"),

path("user_profile/" , views.user_profile, name="user_profile"),

path("index/" , views.home, name="index"),

path("all_status/" , views.all_status, name="all_status"),

path("approved_status/" , views.approved_status, name="approved_status"),

path("consumer_finance/" , views.consumer_finance, name="consumer_finance"),

path("forget_password/" , views.forget_password, name="forget_password"),

path("home_loan/" , views.home_loan, name="home_loan"),

path("in_process_status/" , views.in_process_status, name="in_process_status"),

path("instant_salary/" , views.instant_salary, name="instant_salary"),

path("leads_collected/" , views.leads_collected, name="leads_collected"),

path("micro_finance/" , views.micro_finance, name="micro_finance"),

path("pending_status/" , views.pending_status, name="pending_status"),

path("rejected_status/" , views.rejected_status, name="rejected_status"),

path("team_sspn/" , views.team_sspn, name="team_sspn"),

path("report_error/" , views.report_error, name="report_error"),

path('update/<int:pk>',views.LeadUpdateView.as_view(), name='leads_update'),

path('delete/<int:pk>',views.LeadDeleteView.as_view(), name='leads_delete'),

path('teamupdate/<int:pk>',views.TeamUpdateView.as_view(), name='teamupdate'),

path('teamdelete/<int:pk>',views.TeamDeleteView.as_view(), name='teamdelete'),

path('teamdelete/<int:pk>',views.TeamDeleteView.as_view(), name='teamdelete'),

path('add/new/team_member', views.add_new_teammember_view.as_view(), name='add_new_team_member'),
]