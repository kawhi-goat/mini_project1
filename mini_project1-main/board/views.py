from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect,Http404
from .models import *
from django.urls import reverse
# Create your views here.

def index(request):
    boards = {'boards': Board.objects.all()}
    return render(request, 'list.html', boards)

def post(request):
    if request.method == "POST":
        author = request.POST['author']
        title = request.POST['title']
        content = request.POST['content']
        board = Board(author=author, title=title, content=content)
        board.save()
        return HttpResponseRedirect(reverse('index'))
    else:
        return render(request,'post.html')

def detail(request, id):
    try:
        board = Board.objects.get(pk=id)
    except Board.DoesNotExist:
        raise Http404("Does not exist!")
    return render(request, 'detail.html', {'board': board})
