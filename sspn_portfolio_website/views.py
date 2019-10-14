from django.shortcuts import render

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

def blog_list(request):
    return render(request,'sspn_portfolio_website/blog.html')

def blog_detail(request):
    return render(request,'sspn_portfolio_website/blog_details.html')

def career(request):
    return render(request,'sspn_portfolio_website/career.html')

def signup_registration(request):
    return render(request,'sspn_portfolio_website/register.html')

def detailed_registration(request):
    return render(request,'sspn_portfolio_website/register1.html')

def homeloan(request):
    return render(request,'sspn_portfolio_website/product_details2.html')