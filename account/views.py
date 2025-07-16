from django.shortcuts import render,redirect
from .models import User,UserProfile
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import Club
# Create your views here.
def login_view(request):
    if request.method == 'GET':
        return render(request, 'client/login.html')
    else:
        data = request.POST
        if 'email' not in data:
            messages.error(request, 'Please Provide Email.')
            return redirect("/account/login/")
        if 'password' not in data:
            messages.error(request, 'Please Type Password :) ')
            return redirect("/account/login/")
        email = request.POST['email']
        password = request.POST['password']
        print(f'Email : {email}, Password : {password}')
        if not User.objects.filter(email=email).exists():
            messages.error(request, 'Invalid Email')
            return redirect("/account/login/")
        user = authenticate(email=email, password=password)
        if user is None:
            messages.error(request,"Invalid Password")
            return redirect("/account/login/")
        else:
            login(request,user)
            return redirect('/')

def register(request):
    if request.method=='GET':
        return render(request, 'client/register.html',{"clubs": Club.objects.all()})
    else:
        data = request.POST
        fields = ['email', 'password', 'sponsor_email', 'phone', 'club']

        for i in fields:
            if i not in data:
                messages.error(request, f'Please Provide {i}')
                return redirect("/account/register/")
            if data[i] == None or data[i]=="":
                messages.error(request, f'Please Type {i}')
                return redirect("/account/register/")
        
        if User.objects.filter(email=request.POST['email']).exists():
            messages.error(request, 'Email Already Used.')
            return redirect("/account/register/")
        
        if not User.objects.filter(email=request.POST['sponsor_email']).exists():
            messages.error(request, 'Sponsor Email Not Found.')
            return redirect("/account/register/")

        user = User.objects.create(email = request.POST['email'])
        user.set_password(request.POST['password'])
        user.save()

        profile = UserProfile.objects.create(user = user, phone = request.POST['phone'], sponsor_email = request.POST['sponsor_email'])

        profile.club.set(request.POST['club'])

        return redirect("/account/login/")
    

def logout_view(request):

    logout(request)
    return redirect("/")