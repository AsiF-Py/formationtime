from django.shortcuts import render,redirect,HttpResponse
from .forms import RegisterForm,LoginForm,UserProfileUpdateForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import Account,Company
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def home(request):
    return render(request,'home.html')
@login_required
def dashboard(request):
    try:
        company = Company.objects.get(user=request.user)
        return render(request, 'account/dashbored.html', {'company': company})
    except ObjectDoesNotExist:
        return render(request,'account/dashbored.html')

def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request,'account/register.html',{'form':form})

def login_view(request):
    form = LoginForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('profile')
    return render(request,'account/login.html',{'form':form})

@login_required
def profile(request):
    user = Account.objects.get(username=request.user.username)
    if request.method == 'POST':
        form = UserProfileUpdateForm(request.POST, instance=user)

        if form.is_valid():
            old_password = form.cleaned_data.get('old_password')
            new_password1 = form.cleaned_data.get('new_password1')
            new_password2 = form.cleaned_data.get('new_password2')

            if old_password and new_password1 and new_password2:
                user.set_password(new_password1)
                user.save()
                update_session_auth_hash(request, user)  # To prevent the user from being logged out
                messages.success(request, 'Your account has been updated Successfully.')
                return redirect('profile')  # or wherever you want to redirect after changing the password

            form.save()
            return redirect('profile')  # or wherever you want to redirect after updating the profile
    else:
        form = UserProfileUpdateForm(instance=user)
    return render(request,'account/profile.html',{'user':user,'form':form})

def logout_view(request):
    logout(request)
    return redirect('login')





