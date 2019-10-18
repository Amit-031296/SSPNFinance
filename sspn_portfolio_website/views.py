from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from sspn_lead_manager_app.models import AllLeads,Team
from django.core.mail import send_mail

# Create your views here.

#<--- Pages Views --->

#home page view
def home(request):
    return render(request,'sspn_portfolio_website/index.html')

#<---product page View --->
#product page view
def product_list(request):
    return render(request,'sspn_portfolio_website/product_list.html')

#on product page--microfinance page view
def microfinance(request,product_name):
    data = {'product_name':product_name}
    return render(request,'sspn_portfolio_website/product_details.html',data)

#on product page--homeloan page view
def homeloan(request):
    return render(request,'sspn_portfolio_website/product_details2.html')

#on product page--instantsalary page view
def instantsalary(request,product_name):
    data = {'product_name':product_name}
    return render(request,'sspn_portfolio_website/product_details3.html',data)

#on product page--consumerfinance page view
def consumerfinance(request,product_name):
    data = {'product_name':product_name}
    return render(request,'sspn_portfolio_website/product_details4.html',data)
#</---product page view --->

#aboutus page view
def about_us(request):
    return render(request,'sspn_portfolio_website/about_us.html')

#contactus page view
def contact_us(request):
    return render(request,'sspn_portfolio_website/contact.html')

#contactussuccess page view
def contact_us_success(request):
    return render(request, 'sspn_portfolio_website/contact_us_success.html')

#bloglist page view
def blog_list(request):
    return render(request,'sspn_portfolio_website/blog.html')

#blog page view
def blog_detail(request):
    return render(request,'sspn_portfolio_website/blog_details.html')

#career page view
def career(request):
    return render(request,'sspn_portfolio_website/career.html')

#microfinance,instantsalary,consumerfinance getconnected register page view
def signup_registration(request,product_name):
    data = {'product_name':product_name}
    return render(request,'sspn_portfolio_website/register.html',data)

#detailed registration page view
def detailed_registration(request,pk):
    lead_object = AllLeads.objects.get(pk=int(pk))
    product_name = lead_object.product_interested_in
    data = {'user_pk': pk,
             'product_name':product_name}
    return render(request,'sspn_portfolio_website/register1.html',data)

#</--- Pages views --->

#------ All Form Submit Processing view -----------
#contactus form submit view
def contact_us_submit(request):
    if request.method == "POST":
        yourName = request.POST['yourName']
        yourEmail = request.POST['yourEmail']
        yourPhone = request.POST['yourPhone']
        comments = request.POST['comments']
    send_mail(yourName,yourEmail,'amitv.mumbaii@gmail.com',['sangramtambe2211@gmail.com'],fail_silently=False,)
    
    return HttpResponseRedirect(reverse('sspn_portfolio_website:contact_us_success'))

#detailed registration form submit view
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

#signup registeration form submit view
def signup_registeration_form_submit(request,product_name):
    if request.method == "POST":
        yourName = request.POST['yourName']
        yourEmail = request.POST['yourEmail']
        yourPhone = request.POST['yourPhone']
        product_interested = request.POST['product_interested']
        AllLeads.objects.create(full_name = yourName,
        email = yourEmail,
        contact = yourPhone,
        product_interested_in = product_interested)
        latest_object = AllLeads.objects.latest('date_of_entry')
        latest_pk = latest_object.pk
        return HttpResponseRedirect(reverse('sspn_portfolio_website:detailed_registration',kwargs={'pk': latest_pk }))

#</------ All Form Submit Processing view ----------- 








