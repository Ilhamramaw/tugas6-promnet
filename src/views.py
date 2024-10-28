from django.shortcuts import render
from django.http import HttpResponse

def navbar(request):
  return render(request, 'navbar.html')

def index(request):
  return render(request, 'index.html')

def education(request):
  return render(request, 'pendidikan.html')

def experience(request):
  return render(request, 'pengalaman.html')