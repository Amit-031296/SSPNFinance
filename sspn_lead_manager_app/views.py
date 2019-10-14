from django.shortcuts import render

# Create your views here.
def login(request):
    data = {}
    return render(request,'sspn_lead_manager_app/login.html',data)

def register(request):
    data = {}
    return render(request,'sspn_lead_manager_app/register.html',data)

def home(request):
    data = {}
    return render(request,'sspn_lead_manager_app/Dashboard_sspn.html',data)

def all_status(request):
    data = {}
    return render(request,'sspn_lead_manager_app/all_status.html',data)

def approved_status(request):
    data = {}
    return render(request,'sspn_lead_manager_app/approved_status.html',data)

def consumer_finance(request):
    data = {}
    return render(request,'sspn_lead_manager_app/consumer_finance.html',data)

def forget_password(request):
    data = {}
    return render(request,'sspn_lead_manager_app/forgetPassword.html',data)

def home_loan(request):
    data = {}
    return render(request,'sspn_lead_manager_app/home_loan.html',data)    

def in_process_status(request):
    data = {}
    return render(request,'sspn_lead_manager_app/in_process_status.html',data)    

def instant_salary(request):
    data = {}
    return render(request,'sspn_lead_manager_app/instant_salary.html',data)


def leads_collected(request):
    data = {}
    return render(request,'sspn_lead_manager_app/Leads_Collected.html',data)

def micro_finance(request):
    data = {}
    return render(request,'sspn_lead_manager_app/micro_finance.html',data)

def pending_status(request):
    data = {}
    return render(request,'sspn_lead_manager_app/pending_status.html',data)
    
def rejected_status(request):
    data = {}
    return render(request,'sspn_lead_manager_app/rejected_status.html',data)
    
def report_error(request):
    data = {}
    return render(request,'sspn_lead_manager_app/reportError.html',data)
    
def team_sspn(request):
    data = {}
    return render(request,'sspn_lead_manager_app/team_sspn.html',data)
    
def user_profile(request):
    data = {}
    return render(request,'sspn_lead_manager_app/user_profile.html',data)