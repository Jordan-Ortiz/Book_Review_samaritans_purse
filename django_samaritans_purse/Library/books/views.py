from django.shortcuts import redirect, render, reverse
from django.contrib import messages
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import DetailView
from .models import BookReview, FavoriteBook
import requests

# Create your views here.

"""
Home: Search By Author and Add Review

"""


def home(request):
    if request.method == 'POST':
        author = request.POST['author']
        url = f'https://www.googleapis.com/books/v1/volumes?q=+inauthor:{author}&key=AIzaSyB6Z5mdvSohshY0VhSmArRoKkDOjZNG7b8'
        r = requests.get(url)
        books = r.json()
        if books["totalItems"] == 0:
            messages.warning(request, f'No author found by {author}, please try another author')
            content = {
                'books': 'none'
            }
        else:
            messages.info(request, f'Books by {author}')
            content = {
                'books': books['items']
            }
    else:
        content = {
            'books': 'none'
        }
    return render(request, 'books/home.html', content)


"""
Create Review About A Book 


"""


class CreateBookReview(LoginRequiredMixin, CreateView):
    model = BookReview
    fields = ['rating', 'review']
    template_name = 'books/book_review.html'
    success_url = '/my_review_list/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        book_id = self.kwargs['id']
        form.instance.book_id = book_id
        url = f'https://www.googleapis.com/books/v1/volumes/{book_id}?key=AIzaSyB6Z5mdvSohshY0VhSmArRoKkDOjZNG7b8'
        r = requests.get(url)
        book = r.json()
        form.instance.title = book['volumeInfo']['title']
        form.save()
        return super(CreateBookReview, self).form_valid(form)


def create_review(request):
    if request.method == 'POST':
        book = request.POST['book_name']
        book_id = request.POST['book_id']
        stars = request.POST['stars']
        body = request.POST['review']
        user = request.user
        b = BookReview(book_id=book_id, title=book, rating=stars, review=body, user=user)
        b.save()
        messages.success(request, f'Your review on {book} was successful ')
        return redirect('detail-review', book_id)
    else:
        messages.danger(request, f'Something Happened Please Try Again')
        return redirect('home')

    url = f'https://www.googleapis.com/books/v1/volumes/{id}?key=AIzaSyB6Z5mdvSohshY0VhSmArRoKkDOjZNG7b8'
    r = requests.get(url)
    book = r.json()
    reviews = BookReview.objects.filter(book_id=id)
    content = {
        'book': book,
        'reviews': reviews
    }
    return render(request, 'books/book_details.html', content)


"""
            Make A Favorite Book 
"""


def create_favorite(request, id):
    user = request.user
    url = f'https://www.googleapis.com/books/v1/volumes/{id}?key=AIzaSyB6Z5mdvSohshY0VhSmArRoKkDOjZNG7b8'
    r = requests.get(url)
    book = r.json()
    fb = FavoriteBook(book_id=id, data=book, user=user)
    fb.save()
    messages.success(request, f'Book Added To Favorites')
    return redirect('home')


"""
        Book Details 

"""


class BookDetailView(DetailView):
    model = BookReview
    template_name = 'books/review_details.html'
    context_object_name = 'reviews'


def book_details(request, id):
    url = f'https://www.googleapis.com/books/v1/volumes/{id}?key=AIzaSyB6Z5mdvSohshY0VhSmArRoKkDOjZNG7b8'
    r = requests.get(url)
    book = r.json()
    reviews = BookReview.objects.filter(book_id=id)
    content = {
        'book': book,
        'reviews': reviews
    }
    return render(request, 'books/book_details.html', content)



"""
    Review List

"""


class ListReviews(ListView):
    model = BookReview
    template_name = 'books/reviews.html'
    paginate_by = 4


class FavoriteBookList(ListView):
    model = FavoriteBook
    template_name = 'books/favorite_list.html'
    paginate_by = 4

    def get_queryset(self):
        queryset = FavoriteBook.objects.filter(user=self.request.user)
        return queryset


class MyReviewList(LoginRequiredMixin, ListView):
    model = BookReview
    template_name = 'books/my_reviews.html'
    paginate_by = 4

    def get_queryset(self):
        queryset = BookReview.objects.filter(user=self.request.user)
        return queryset


"""
Delete And Update Reviews

"""


class UpdateReview(UpdateView):
    model = BookReview
    fields = ['rating', 'review']
    template_name_suffix = '_update'
    success_url = '/my_review_list/'


class DeleteReview(DeleteView):
    model = BookReview
    success_url = '/my_review_list/'
