from django.shortcuts import render,redirect
from .models import customer,products_desc
# Create your views here.
def index(request):
    daily_prd=products_desc.objects.filter(daily_products=True)
    nondaily_prd=products_desc.objects.filter(daily_products=False)
    return render(request,'index.html',{'daily_prd':daily_prd,'nondaily_prd':nondaily_prd})
    
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def cows(request):
    return render(request,'cows.html')
def products(request):
    return render(request,'products.html')
def gallery(request):
    return render(request,'gallery.html')
def messag(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        num = request.POST['num']
        sub = request.POST['sub']
        mes = request.POST['mes']

        customer.objects.create(name = name,email = email,num = num,sub = sub,mes = mes)
        return redirect('messages')

    return render(request,'contact.html')
    