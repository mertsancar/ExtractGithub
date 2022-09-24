from django.http import HttpResponseRedirect
from django.shortcuts import render
from searchGithub.database import get_github_candidates

from .scraperGithub import extract_github
from .forms import NameForm

searchKeyword = ""

def home(request):
    return render(request, "index.html")


def searchGithub(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'searchGithub.html', {'form': form})


def users(request):

    if request.method == 'POST':
        extract_github(request.POST["searchKeyword"])
        usersdata = get_github_candidates(request.POST["searchKeyword"])
        data = {"usersdata" : usersdata}

    return render(request, "users.html", data)