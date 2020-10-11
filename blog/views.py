from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(self):
	return HttpResponse('<h1>Blog home</h1>')

def about(self):
	return HttpResponse('<h1>Blog about page</h1>')

