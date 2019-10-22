from django.views import generic
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.hashers import make_password
from bootstrap_modal_forms.generic import (BSModalCreateView,
                                           BSModalUpdateView,
                                           BSModalReadView,
                                           BSModalDeleteView)

from sspn_lead_manager_app.models import AllLeads,Team 
from sspn_lead_manager_app.forms import AllLeadsForm,TeamForm    





# Create your views here.
def user_sign_in(request):
    """Logs in a user if the credentials are valid and the user is active, 
    else redirects to the same page and displays an error message."""
    if request.method == "POST":
        username =  request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('sspn_lead_manager_app:index'))   
        else:
            return render(request, 'sspn_lead_manager_app/registration/login.html',{'error_message': 'Username or Password Incorrect!'})

    else:
        return render(request, 'sspn_lead_manager_app/registration/login.html')
    

def register(request):
    if request.method == "POST":
        username =  request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password != confirm_password:
            return render(request, 'sspn_lead_manager_app/registration/register.html',{'error_message':'Passwords do not match!'})
        if Team.objects.filter(username = username).exists():
            return render(request, 'sspn_lead_manager_app/registration/register.html',{'error_message':'Username already exists!'})
        else:
            # Role 2 is for admin, 1 is for super admin.
            user = Team.objects.create(username=username, password= make_password(password),role=2)
            login(request, user)
            return HttpResponseRedirect(reverse('sspn_lead_manager_app:index'))
    else:
        return render(request, 'sspn_lead_manager_app/registration/register.html')

def user_sign_out(request):
    logout(request)
    return HttpResponseRedirect(reverse('sspn_lead_manager_app:login')) 
    
@login_required(login_url='/user_login')
def home(request):
    user_role = request.user.role 
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
    "city_other_count":city_other_count,
    "user_role":user_role}
    return render(request,'sspn_lead_manager_app/Dashboard_sspn.html',data)

@login_required(login_url='/user_login')
def all_status(request):
    user_role = request.user.role 
    all_status = AllLeads.objects.all()
    data = {'all_status':all_status,'user_role':user_role}
    return render(request,'sspn_lead_manager_app/all_status.html',data)

@login_required(login_url='/user_login')
def approved_status(request):
    user_role = request.user.role 
    approved_status = AllLeads.objects.all().filter(status='Approved')
    data = {'approved_status':approved_status,'user_role':user_role}
    return render(request,'sspn_lead_manager_app/approved_status.html',data)

@login_required(login_url='/user_login')
def consumer_finance(request):
    user_role = request.user.role 
    product_consumer_finance = AllLeads.objects.all().filter(product_interested_in='ConsumerFinance')
    data = {'product_consumer_finance':product_consumer_finance,'user_role':user_role}
    return render(request,'sspn_lead_manager_app/consumer_finance.html',data)

@login_required(login_url='/user_login')
def forget_password(request):
    data = {}
    return render(request,'sspn_lead_manager_app/forgetPassword.html',data)

@login_required(login_url='/user_login')
def home_loan(request):
    data = {}
    return render(request,'sspn_lead_manager_app/home_loan.html',data)    

@login_required(login_url='/user_login')
def in_process_status(request):
    user_role = request.user.role 
    in_process_status = AllLeads.objects.all().filter(status='InProcess')
    data = {'in_process_status':in_process_status,'user_role':user_role}
    return render(request,'sspn_lead_manager_app/in_process_status.html',data)    

@login_required(login_url='/user_login')
def instant_salary(request):
    user_role = request.user.role 
    product_instantsalary = AllLeads.objects.all().filter(product_interested_in='InstantSalary')
    data = {'product_instantsalary':product_instantsalary,'user_role':user_role}
    return render(request,'sspn_lead_manager_app/instant_salary.html',data)


@login_required(login_url='/user_login')
def leads_collected(request):
    user_role = request.user.role 
    leads = AllLeads.objects.all()
    data = {'leads':leads,'user_role':user_role}
    return render(request,'sspn_lead_manager_app/Leads_Collected.html',data)

@login_required(login_url='/user_login')
def micro_finance(request):
    user_role = request.user.role 
    product_microfinance = AllLeads.objects.all().filter(product_interested_in='MicroFinance')
    data = {'product_microfinance':product_microfinance,'user_role':user_role}
    return render(request,'sspn_lead_manager_app/micro_finance.html',data)

@login_required(login_url='/user_login')
def pending_status(request):
    user_role = request.user.role 
    pending_status = AllLeads.objects.all().filter(status='Pending')
    data = {'pending_status':pending_status,'user_role':user_role}
    return render(request,'sspn_lead_manager_app/pending_status.html',data)
    
@login_required(login_url='/user_login')
def rejected_status(request):
    user_role = request.user.role
    rejected_status = AllLeads.objects.all().filter(status='Rejected')
    data = {'rejected_status':rejected_status,'user_role':user_role}
    return render(request,'sspn_lead_manager_app/rejected_status.html',data)

@login_required(login_url='/user_login')  
def report_error(request):
    data = {}
    return render(request,'sspn_lead_manager_app/reportError.html',data)

@login_required(login_url='/user_login')  
def team_sspn(request):
    team_sspn = Team.objects.all()
    data = {'team_sspn':team_sspn}
    return render(request,'sspn_lead_manager_app/team_sspn.html',data)

@login_required(login_url='/user_login')   
def user_profile(request):
    user_name = request.user.username 
    user_email = request.user.email
    user_id = request.user.pk
    contact = request.user.contact
    data = {'user_name':user_name,
    'user_email':user_email,
    'user_id':user_id,
    'contact':contact} 
    return render(request,'sspn_lead_manager_app/user_profile.html',data)

@method_decorator(login_required, name='dispatch')
class LeadProductUpdateView(BSModalUpdateView):
    model = AllLeads
    template_name = 'sspn_lead_manager_app/update_entry.html'
    form_class = AllLeadsForm
    success_message = 'Success: Entry was updated.'
    def get_success_url(self,**kwargs):
        leads_object = AllLeads.objects.get(pk=self.kwargs['pk'])
        product_name = leads_object.product_interested_in
        return reverse_lazy('sspn_lead_manager_app:'+product_name)

@method_decorator(login_required, name='dispatch')
class LeadStatusUpdateView(BSModalUpdateView):
    model = AllLeads
    template_name = 'sspn_lead_manager_app/update_entry.html'
    form_class = AllLeadsForm
    success_message = 'Success: Entry was updated.'
    def get_success_url(self,**kwargs):
        leads_object = AllLeads.objects.get(pk=self.kwargs['pk'])
        status_name = leads_object.status
        return reverse_lazy('sspn_lead_manager_app:'+status_name)

@method_decorator(login_required, name='dispatch')
class LeadUpdateView(BSModalUpdateView):
    model = AllLeads
    template_name = 'sspn_lead_manager_app/update_entry.html'
    form_class = AllLeadsForm
    success_message = 'Success: Entry was updated.'
    success_url = reverse_lazy('sspn_lead_manager_app:leads_collected')

@method_decorator(login_required, name='dispatch')
class LeadAllStatusUpdateView(BSModalUpdateView):
    model = AllLeads
    template_name = 'sspn_lead_manager_app/update_entry.html'
    form_class = AllLeadsForm
    success_message = 'Success: Entry was updated.'
    success_url = reverse_lazy('sspn_lead_manager_app:all_status')


@method_decorator(login_required, name='dispatch')
class LeadProductDeleteView(BSModalDeleteView):
    model = AllLeads
    template_name = 'sspn_lead_manager_app/delete_entry.html'
    success_message = 'Success: Entry was deleted.'
    def get_success_url(self,**kwargs):
        leads_object = AllLeads.objects.get(pk=self.kwargs['pk'])
        product_name = leads_object.product_interested_in
        return reverse_lazy('sspn_lead_manager_app:'+product_name)

@method_decorator(login_required, name='dispatch')
class LeadStatusDeleteView(BSModalDeleteView):
    model = AllLeads
    template_name = 'sspn_lead_manager_app/delete_entry.html'
    success_message = 'Success: Entry was deleted.'
    def get_success_url(self,**kwargs):
        leads_object = AllLeads.objects.get(pk=self.kwargs['pk'])
        status_name = leads_object.status
        return reverse_lazy('sspn_lead_manager_app:'+status_name)


@method_decorator(login_required, name='dispatch')
class LeadDeleteView(BSModalDeleteView):
    model = AllLeads
    template_name = 'sspn_lead_manager_app/delete_entry.html'
    success_message = 'Success: Entry was deleted.'
    success_url = reverse_lazy('sspn_lead_manager_app:leads_collected')

@method_decorator(login_required, name='dispatch')
class LeadAllStatusDeleteView(BSModalDeleteView):
    model = AllLeads
    template_name = 'sspn_lead_manager_app/delete_entry.html'
    success_message = 'Success: Entry was deleted.'
    success_url = reverse_lazy('sspn_lead_manager_app:all_status')


@method_decorator(login_required, name='dispatch')
class TeamUpdateView(BSModalUpdateView):
    model = Team
    template_name = 'sspn_lead_manager_app/update_entry.html'
    form_class = TeamForm
    success_message = 'Success: Entry was updated.'
    success_url = reverse_lazy('sspn_lead_manager_app:team_sspn')

@method_decorator(login_required, name='dispatch')
class TeamDeleteView(BSModalDeleteView):
    model = Team
    template_name = 'sspn_lead_manager_app/delete_entry.html'
    success_message = 'Success: Entry was deleted.'
    success_url = reverse_lazy('sspn_lead_manager_app:team_sspn')

@method_decorator(login_required, name='dispatch')
class add_new_teammember_view(BSModalCreateView):
    template_name = 'sspn_lead_manager_app/add_new_teammember.html'
    form_class = TeamForm
    success_message = 'Success: New Team Member was added.'
    success_url = reverse_lazy('sspn_lead_manager_app:team_sspn')

def error_404_view(request, exception):
    data = {"name": "ThePythonDjango.com"}
    return render(request,'/registration/login.html', data)