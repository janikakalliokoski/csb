# from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# test_user1 sunshine100
# test_user2 sunshine200


@login_required
def homeView(request):
    return render(request, "pages/index.html")

