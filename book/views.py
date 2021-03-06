from audioop import reverse
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.shortcuts import render
from book.models import Book
from book import models, forms
from django.views import generic

# class BookListView(generic.ListView):
#     template_name = 'book_list.html'
#     queryset = models.Book.objects.all()
#
#     def get_queryset(self):
#         return models.Book.objects.all()


def get_books(request):
    book = models.Book.objects.all()
    return render(request, 'book_list.html', {'book': book})


# class BookDetailView(generic.DetailView):
#     template_name = 'books_detail.html'
#
#     def get_object(self, **kwargs):
#         book_id = self.kwargs.get("id")
#         return get_object_or_404(models.Book, id=book_id)


def books_detail(request, id):
    books = get_object_or_404(models.Book, id=id)
    return render(request, 'books_detail.html', {'books': books})



def add_book(request):
    method = request.method
    if method == 'POST':
        form = forms.BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # return HttpResponse('Book created')
            return redirect(reverse('books:books_all'))
    else:
        form = forms.BookForm()
    return render(request, 'add_book.html', {'form': form})



def book_update(request, id):
    book_object = get_object_or_404(models.Book, id=id)
    if request.method == "POST":
        form = forms.BookForm(instance=book_object, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Book Updated Successfully")
            # return redirect(reverse("books:books_all"))
    else:
        form = forms.BookForm(instance=book_object)
    return render(request, "book_update.html", {"form": form, "object": book_object})


def book_delete(request, id):
    book_object = get_object_or_404(models.Book, id=id)
    book_object.delete()
    return HttpResponse('Show Deleted')


