from django.shortcuts import render , redirect ,HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

# Create your views here.



def Register_page(request):
    if request.method == "POST":
        name = request.POST['Name']
        email = request.POST['Email']
        phone_number = request.POST['Number']
        username = request.POST['Username']
        password = request.POST['password']

        if len(phone_number) !=10:
            messages.error(request,'Phone Number should be 10 Digit')
            return redirect('register')
        
        user = User.objects.filter(username = username)
        if user.exists():
            messages.error(request,'Username already exists')
            return redirect('register')
        
        user = User.objects.create_user(username,email,password,first_name=name)
        user.save()
        messages.success(request,'Account created Successfully')
        return redirect('login')
 
    return render(request,"accounts/register.html")

def Login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username = username).exists():
            messages.error(request,'Invalid username')
            return redirect('login')

        user = authenticate(username = username,password= password)
        
        if user is None:
            messages.error(request,'Invalid Password')
            return redirect('login')


        if user is not None:
            login(request,user)
            return redirect('/')
    return render(request,"accounts/login.html")

def Logout_page(request):
    logout(request)
    return redirect('login')

    



