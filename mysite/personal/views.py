from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from .forms import NewUserForm
# Create your views here.
# Create your views here.
def homepage(request):
#    return HttpResponse("Wow <strong>So Amazing</strong> website #amaze.")
    return render(request=request, 
                  template_name="personal/loginpage.html",)


    
def login_request(request):
    if request.method=="POST":
        form = AuthenticationForm(request = request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return render(request = request,
                             template_name = "personal/index.html")
                
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
  
    form = AuthenticationForm()
    return render(request = request,
                  template_name = "personal/loginpage.html",
                  context={"form":form})



def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"New Account Created: {username}")
            login(request, user)
            return render(request=request, 
                          template_name="personal/loginpage.html",)
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")

            return render(request = request,
                          template_name = "personal/register.html",
                          context={"form":form})
    form = NewUserForm
    return render(request = request,
                  template_name = "personal/register.html",
                  context={"form":form})
