from django.db.models import Count
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.views import View
from . models import Product,Customer
# from . forms import CustomerProfileForm  
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# from . forms import CustomerRegistrationForm

# Create your views here.
def Index(request):
    return render(request,"index.html")

class CategoryView(View):
    def get(self,request,val):
        product = Product.objects.filter(category = val)
        title = Product.objects.filter(category = val).values('title')
        return render(request,"category.html",locals()) 
    
class ProductDetail(View):
    def get(self,request,pk):
        product = Product.objects.get(pk=pk)
        return render(request,"product-detail.html",locals())
    

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        if pass1!=pass2:
            messages.warning(request,("Your password and confrom password are not Same!!"))
            return render(request,"customerregistration.html") 
        try:
            if User.objects.get(username=uname):
                messages.warning(request,("user is already exist"))
                return render(request,"customerregistration.html") 
        except Exception as identifier:
                pass
        
        my_user=User.objects.create_user(uname,email,pass1)
        my_user.save()
        messages.success(request,("account created successfully"))
        return redirect('/login')
    return render(request,"customerregistration.html") 


def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            messages.warning(request,("Username or Password is incorrect!!!"))
            return render (request,'/login')
    else:
        return render(request,'login.html')  

def ProfilePage(request):
    if request.method=='POST':
        user = request.user
        name = request.POST.get('username')
        locality = request.POST.get('locality')
        city = request.POST.get('city')
        mobile = request.POST.get('phone')
        state = request.POST.get('state')
        zipcode = request.POST.get('zipcode')
        reg = Customer(user = user,name = name,locality = locality,city = city,mobile = mobile,state = state,zipcode = zipcode)
        reg.save()
        if reg is not None:
            messages.success(request,("Profile Updated Successfully"))
            return redirect('/profile')
        else:
            messages.warning(request,("please fill the form correctly"))
            return render(request,'profile.html')

    return render(request,'profile.html')

def Logout(request):
    logout(request)
    messages.success(request,("Logout Successfully"))
    return redirect('/')
    
    
def AddressPage(request):
    add = Customer.objects.filter(user = request.user)
    return render(request,'address.html',locals())
  
    

def UpdatePage(request,pk):
    if request.method=='POST':
        add = Customer.objects.get(pk=pk)
        add.name = request.cleaned_data('username')
        add.locality = request.cleaned_data('locality')
        add.city = request.cleaned_data('city')
        add.mobile = request.cleaned_data('phone')
        add.state = request.cleaned_data('state')
        add.zipcode = request.cleaned_data('zipcode')
        add.reg.save()
        if reg is not None:
            messages.success(request,("Profile Updated Successfully"))
            return redirect('/profile')
        else:
            messages.warning(request,("please fill the form correctly"))
            return render(request,'profile.html')

    return render(request,'updateaddress.html',locals())
