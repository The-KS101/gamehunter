from django.shortcuts import render, HttpResponse, redirect
from .forms import gameSearched
from . import GetSimilar
import re


# Create your views here.
def index(request):

    return render(request, 'index.html' )

