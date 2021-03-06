from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

from django.http import HttpResponse

def register(request):

    #If the user exists, or is logged in, the system throws
    # and error and the site crashes
    # TODO: Update reg form to account for logged / existing users


    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = UserCreationForm()

        context = {'form': form}
        return render(request, 'users/register.html', context)


def success(request):

    context = {
    'user': request.user
    }
    return render(request, 'users/success.html', context)
