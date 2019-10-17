from django.shortcuts import render
from sspn_lead_manager_app.models import AllLeads,Team
from bootstrap_modal_forms.generic import (BSModalCreateView,
                                           BSModalUpdateView,
                                           BSModalReadView,
                                           BSModalDeleteView)
from django.urls import reverse_lazy, reverse
from sspn_lead_manager_app.models import AllLeads,Team 
from sspn_lead_manager_app.forms import AllLeadsForm,TeamForm    
from django.db.models import Count, Q

# Create your views here.
def login(request):
    data = {}
    return render(request,'sspn_lead_manager_app/login.html',data)

def register(request):
    data = {}
    return render(request,'sspn_lead_manager_app/register.html',data)

def home(request):
    salaried_count = AllLeads.objects.filter(profession="Salaried").all().count()
    business_count = AllLeads.objects.filter(profession="Business").all().count()
    self_employed_count = AllLeads.objects.filter(profession="Self Employed").all().count()
    other_count = AllLeads.objects.filter(profession="Other").all().count()
    micro_finance_count = AllLeads.objects.filter(product_interested_in="Micro Finance").all().count()
    instant_salary_count = AllLeads.objects.filter(product_interested_in="Instant Salary").all().count()
    consumer_finance_count = AllLeads.objects.filter(product_interested_in="Consumer Finance").all().count()
    city_mumbai_count = AllLeads.objects.filter(city="Mumbai").all().count()
    city_delhi_count = AllLeads.objects.filter(city="Delhi").all().count()
    city_banglore_count = AllLeads.objects.filter(city="Banglore").all().count()
    city_pune_count = AllLeads.objects.filter(city="Pune").all().count()
    city_ahmedabad_count = AllLeads.objects.filter(city="Ahmedabad").all().count()
    city_other_count = AllLeads.objects.filter(city="Other").all().count()
    data = {"micro_finance_count":micro_finance_count,
    "instant_salary_count":instant_salary_count,
    "consumer_finance_count":consumer_finance_count,
    "salaried_count":salaried_count,
    "business_count":business_count,
    "self_employed_count":self_employed_count,
    "other_count":other_count,
    "city_mumbai_count":city_mumbai_count,
    "city_delhi_count":city_delhi_count,
    "city_banglore_count":city_banglore_count,
    "city_pune_count":city_pune_count,
    "city_ahmedabad_count":city_ahmedabad_count,
    "city_other_count":city_other_count}
    return render(request,'sspn_lead_manager_app/Dashboard_sspn.html',data)

def all_status(request):
    all_status = AllLeads.objects.all().filter(status='All Status')
    data = {'all_status':all_status}
    return render(request,'sspn_lead_manager_app/all_status.html',data)

def approved_status(request):
    approved_status = AllLeads.objects.all().filter(status='Approved Status')
    data = {'approved_status':approved_status}
    return render(request,'sspn_lead_manager_app/approved_status.html',data)

def consumer_finance(request):
    product_consumer_finance = AllLeads.objects.all().filter(product_interested_in='Consumer Finance')
    data = {'product_consumer_finance':product_consumer_finance}
    return render(request,'sspn_lead_manager_app/consumer_finance.html',data)

def forget_password(request):
    data = {}
    return render(request,'sspn_lead_manager_app/forgetPassword.html',data)

def home_loan(request):
    data = {}
    return render(request,'sspn_lead_manager_app/home_loan.html',data)    

def in_process_status(request):
    in_process_status = AllLeads.objects.all().filter(status='In Process Status')
    data = {'in_process_status':in_process_status}
    return render(request,'sspn_lead_manager_app/in_process_status.html',data)    

def instant_salary(request):
    product_instantsalary = AllLeads.objects.all().filter(product_interested_in='Instant Salary')
    data = {'product_instantsalary':product_instantsalary}
    return render(request,'sspn_lead_manager_app/instant_salary.html',data)


def leads_collected(request):
    leads = AllLeads.objects.all()
    data = {'leads':leads}
    return render(request,'sspn_lead_manager_app/Leads_Collected.html',data)

def micro_finance(request):
    product_microfinance = AllLeads.objects.all().filter(product_interested_in='Micro Finance')
    data = {'product_microfinance':product_microfinance}
    return render(request,'sspn_lead_manager_app/micro_finance.html',data)

def pending_status(request):
    pending_status = AllLeads.objects.all().filter(status='Pending Status')
    data = {'pending_status':pending_status}
    return render(request,'sspn_lead_manager_app/pending_status.html',data)
    
def rejected_status(request):
    rejected_status = AllLeads.objects.all().filter(status='Rejected Status')
    data = {'rejected_status':rejected_status}
    return render(request,'sspn_lead_manager_app/rejected_status.html',data)
    
def report_error(request):
    data = {}
    return render(request,'sspn_lead_manager_app/reportError.html',data)
    
def team_sspn(request):
    team_sspn = Team.objects.all()
    data = {'team_sspn':team_sspn}
    return render(request,'sspn_lead_manager_app/team_sspn.html',data)
    
def user_profile(request):
    user_name = request.user.username 
    user_email = request.user.email
    user_id = request.user.pk
    data = {'user_name':user_name,
    'user_email':user_email,
    'user_id':user_id}
    return render(request,'sspn_lead_manager_app/user_profile.html',data)


class LeadUpdateView(BSModalUpdateView):
    model = AllLeads
    template_name = 'sspn_lead_manager_app/update_entry.html'
    form_class = AllLeadsForm
    success_message = 'Success: Entry was updated.'
    success_url = reverse_lazy('sspn_lead_manager_app:leads_collected')


class LeadDeleteView(BSModalDeleteView):
    model = AllLeads
    template_name = 'sspn_lead_manager_app/delete_entry.html'
    success_message = 'Success: Entry was deleted.'
    success_url = reverse_lazy('sspn_lead_manager_app:leads_collected')

class TeamUpdateView(BSModalUpdateView):
    model = Team
    template_name = 'sspn_lead_manager_app/update_entry.html'
    form_class = TeamForm
    success_message = 'Success: Entry was updated.'
    success_url = reverse_lazy('sspn_lead_manager_app:team_sspn')


class TeamDeleteView(BSModalDeleteView):
    model = Team
    template_name = 'sspn_lead_manager_app/delete_entry.html'
    success_message = 'Success: Entry was deleted.'
    success_url = reverse_lazy('sspn_lead_manager_app:team_sspn')

class add_new_teammember_view(BSModalCreateView):
    template_name = 'sspn_lead_manager_app/add_new_teammember.html'
    form_class = TeamForm
    success_message = 'Success: New Team Member was added.'
    success_url = reverse_lazy('sspn_lead_manager_app:team_sspn')