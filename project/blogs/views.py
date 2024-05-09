from django.shortcuts import render
from .models import *


# Create your views here.
def home(request):
    Post = post.objects.all()
    context = {
        "post":Post
    }
    return render(request, "index.html", context)