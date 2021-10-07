from django.shortcuts import render
from django.views.generic import (  # ListView,
    # CreateView,
    UpdateView,
    DeleteView
)
from .models import Book
from django.urls import reverse_lazy


def index(request):
    books = Book.objects.all()
    if request.method == 'POST':
        new_book = Book(
            name=request.POST['name'],
            author=request.POST['author'],
            description=request.POST['description'],
        )
        if new_book.name == '' or new_book.author == '' or new_book.description == '':
            pass
        else:
            new_book.save()
    return render(request, 'home.html', {'books': books})


# class BookListView(ListView):
#     model = Book
#     template_name = 'home.html'


# class BookCreateView(CreateView):
#     model = Book
#     template_name = 'create.html'
#     fields = ['name', 'author', 'description']
#     success_url = reverse_lazy('home')


class BookUpdateView(UpdateView):
    model = Book
    template_name = 'update.html'
    fields = ['name', 'description']
    success_url = reverse_lazy('home')


class BookDeleteView(DeleteView):
    model = Book
    template_name = 'delete.html'
    success_url = reverse_lazy('home')
