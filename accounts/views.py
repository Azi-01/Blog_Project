from django.contrib.auth.views import redirect_to_login
from django.shortcuts import render
from .forms import CustomUserCreationForm

# Create your views here.
def signUpView(request):
    if request.method == "POST":
        form = CustomUserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect_to_login('/')
    else:
        form = CustomUserCreationForm()
    
    context = {'form': form}
    return render(request, 'registration/signup.html', context)
