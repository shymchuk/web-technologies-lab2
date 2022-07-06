from django.shortcuts import render
from django.http import *
# Create your views here.


def main(request: HttpRequest):
    return render(request, 'user_chat/index.html')
