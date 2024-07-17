from django.shortcuts import render,redirect
from .models import users,products
from django.contrib import messages
# Create your views here.
def register(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']
        conformpassword=request.POST['conformpassword']
        emailexists=users.objects.filter(Email=email)
        if emailexists :
            messages.error(request,'EMAIL ALREADY EXISTS!')
        elif password!=conformpassword :
            messages.error(request,'PASSWORD IS NOT SAME AS ABOVE!')
        else:
            users(Name=name,Email=email,Password=password).save()
            return redirect('login')
        
    return render(request,'register.html')

def login(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        current_user=users.objects.filter(Email=email,Password=password)
        if current_user :
            request.session['Email']=email
            return redirect('add')
        else:
            messages.error(request,'INVALID EMAIL OR PASSWORD!')
    return render(request,'login.html')

def addproduct(request):
    if 'Email' in request.session:
        current_user=request.session['Email']
        user=users.objects.get(Email=current_user)
        if request.method=='POST':
            productname=request.POST['productname']
            companyname=request.POST['companyname']
            price=request.POST['price']
            image=request.FILES.get('image')
            products(Productname=productname,Companyname=companyname,Price=price,Image=image).save()
            return redirect('read')
    return render(request,'addproduct.html',{'a':current_user,'user':user})

def read(request):
    product=products.objects.all()
    if 'Email' in request.session:
        current_user=request.session['Email']
        user=users.objects.get(Email=current_user)

    return render(request,'read.html',{'product':product,'user':user})

def logout(request):
    del request.session['Email']
    return redirect('login')

def details(request,id):
    details=products.objects.get(id=id)
    return render(request,'details.html',{'details':details})

def update(request,id):
    update=products.objects.get(id=id)
    if request.method=='POST':
        productname=request.POST['productname']
        companyname=request.POST['companyname']
        image=request.FILES.get('image')
        price=request.POST['price']
        update.Productname=productname
        update.Companyname=companyname
        update.Image=image
        update.Price=price
        update.save()
        return redirect('read')
    return render(request,'update.html',{'update':update})