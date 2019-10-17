from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from sspn_lead_manager_app.models import AllLeads,Team
from django.core.mail import send_mail

# Create your views here.
def home(request):
    return render(request,'sspn_portfolio_website/index.html')

def product_list(request):
    return render(request,'sspn_portfolio_website/product_list.html')

def microfinance(request):
    return render(request,'sspn_portfolio_website/product_details.html')

def instantsalary(request):
    return render(request,'sspn_portfolio_website/product_details3.html')

def consumerfinance(request):
    return render(request,'sspn_portfolio_website/product_details4.html')

def about_us(request):
    return render(request,'sspn_portfolio_website/about_us.html')

def contact_us(request):
    return render(request,'sspn_portfolio_website/contact.html')

def contact_us_submit(request):
    if request.method == "POST":
        yourName = request.POST['yourName']
        yourEmail = request.POST['yourEmail']
        yourPhone = request.POST['yourPhone']
        comments = request.POST['comments']
    send_mail(yourName,yourEmail,'amitv.mumbaii@gmail.com',['sangramtambe2211@gmail.com'],fail_silently=False,)
    
    return HttpResponseRedirect(reverse('sspn_portfolio_website:contact_us_success'))

def contact_us_success(request):
    return render(request, 'sspn_portfolio_website/contact_us_success.html')

def blog_list(request):
    return render(request,'sspn_portfolio_website/blog.html')

def blog_detail(request):
    return render(request,'sspn_portfolio_website/blog_details.html')

def career(request):
    return render(request,'sspn_portfolio_website/career.html')

def signup_registration(request,product_name):
    data = {'product_name':product_name}
    return render(request,'sspn_portfolio_website/register.html',data)

def signup_registeration_form_submit(request,product_name):
    if request.method == "POST":
        yourName = request.POST['yourName']
        yourEmail = request.POST['yourEmail']
        yourPhone = request.POST['yourPhone']
        AllLeads.objects.create(full_name = yourName,
        email = yourEmail,
        contact = yourPhone,
        product_interested_in = product_name)
        latest_object = AllLeads.objects.latest('date_of_entry')
        latest_pk = latest_object.pk
    return HttpResponseRedirect(reverse('sspn_portfolio_website:detailed_registration',kwargs={'pk': latest_pk }))





def detailed_registration(request,pk):
    data = {'user_pk': pk }
    return render(request,'sspn_portfolio_website/register1.html',data)

def detailed_registration_submit(request,pk):
    if request.method == "POST":
        yourCity = request.POST['yourCity']
        yourCompany = request.POST['yourCompany']
        yourprofession = request.POST['yourprofession']
        one_lead = AllLeads.objects.get(pk=pk)
        one_lead.city = yourCity
        one_lead.company_name = yourCompany
        one_lead.profession = yourprofession
        one_lead.save()
    return HttpResponseRedirect(reverse('sspn_portfolio_website:index'))

def homeloan(request):
    return render(request,'sspn_portfolio_website/product_details2.html')