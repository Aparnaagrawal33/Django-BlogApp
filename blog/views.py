from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.
'''
def home(request):
	return render(request,'blog/home.html', {'title':'Home'})

def about(request):
	return render(request,'blog/about.html', {'title':'about'})
	'''

'''posts = [
    {
        'author': 'Aparna Agrawal',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2020'
    },
    {
        'author': 'Shriti sharan',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'September 1, 2020'
    }
]'''


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
