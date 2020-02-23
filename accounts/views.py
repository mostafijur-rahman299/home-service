from django.shortcuts import render, redirect

from django.contrib import messages, auth

from django.contrib.auth import get_user_model

User = get_user_model()

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        
        if password == password2:
            if User.objects.filter(username=username).exists(): 
                messages.error(request, 'Username is taken.') 
                return redirect('accounts:register')
            else:
                if User.objects.filter(email=email).exists(): 
                    messages.error(request, 'Email is taken.') 
                    return redirect('accounts:register')
                else:
                    user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                    if user:
                        messages.success(request, 'Registration done.')
                        return redirect('accounts:login')
        else:
            messages.error(request, 'Password do not match.')
            return redirect("accounts:register") 
        
    return render(request, 'accounts/register.html', {})



def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            messages.success(request, 'You are loged in..')
            return redirect('accounts:dashboard')
        else:
            return redirect('accounts:login')
    return render(request, 'accounts/login.html', {})


def logout(request):
    auth.logout(request)
    return redirect("/")

def dashboard(request):
    return render(request, 'accounts/dashboard.html', {})



