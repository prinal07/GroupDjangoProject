from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect

from project.models import User


from .forms import CreateUserForm

# Create your views here.
from django.http import HttpResponse

def index(request):
    return render(request, 'project/index.html')


class registerPage(View):
    form_class = UserCreationForm # or any other form you want to use
  
    initial = {'key': 'value'}
    template_name = 'project/register.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user_username=request.POST['username']
            user_password = request.POST['password2']
            new_user = MyUser.objects.create(user=request.MyUser, username=user_username, password = user_password)
            form.save() 

            new_user.save()

            # <process form cleaned data>
            return HttpResponseRedirect('/success/')
        else:
        # add an error message to the context dictionary
            error_message = "There was an error in the form data. Please correct the errors"
            context = {'form': form, 'error_message': error_message}
            return render(request, self.template_name, context)
    
        return render(request, self.template_name, {'form': form})

def loginPage(request):
    context = {}
    return render(request, 'project/login.html', context)
