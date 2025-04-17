from django.http import HttpResponse
from django.shortcuts import render, redirect
def home(request):
    if request.method=="GET":
        print(request.GET.get("username"))
        print(request.GET.get("userpass"))
        print(name)
        print(userpass)
    return render(request, "index.html",context={"name":"Mayank"})
def login(request):
    return render(request, "login.html")