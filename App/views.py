from django.shortcuts import render
from django.contrib import messages
import pyshorteners

# Create your views here.
def home(request):
    long_url = ''
    short_url = ''
    if request.method == "POST":
        long_url = request.POST['url']
        type_tiny = pyshorteners.Shortener()
        short_url = type_tiny.tinyurl.short(long_url)
        messages.success(request,"Genrated")
    context = {"short_url":short_url,"url":long_url}
    return render(request,'index.html',context)
