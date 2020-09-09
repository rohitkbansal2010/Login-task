from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

from .forms import CustomUserCreationForm
from .models import Account


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


@csrf_exempt
def userList(request):
    users = Account.objects.all()
    return render(request, 'home.html', {'users': users})


def deleteUser(request, user_id):
    user = Account.objects.get(id=user_id)
    user.delete()
    return redirect('userList')

