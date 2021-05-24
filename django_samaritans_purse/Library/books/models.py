from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.

"""
Create a Django app that lists books and allows a user to post a review of a book.
    BookReview(model)
    - book id
    - review
    - user foreign key
     
    User(model)
    - username


The app should use the Google Books API to fetch data by your favorite author and save to the Django database.
    - fetch json data; by author
    
The app should have a reviews table that is associated to the list of books that are saved to the database.
    - pull reviews
    
The app should allow a user to click a button 
to view the details of a book and on that page,
 a user should be able to submit a review.
    - create review and write review
    
Details page should have Title, Author, Image, description and published date
    - detail page about each review by id

"""


class BookReview(models.Model):
    class Stars(models.IntegerChoices):
        Do_Not_Pick_This_Up_1_star = 1
        Just_Did_Not_Like_it_2_stars = 2
        Mixed_Feelings_3_stars = 3
        Enjoyed_It_4_stars = 4
        New_Favorite_5_stars = 5
    book_id = models.CharField(max_length=200, null=True)
    image_url = models.URLField(null=True, blank=True)
    title = models.CharField(max_length=200, null=True)
    rating = models.IntegerField(null=True, blank=True, choices=Stars.choices)
    review = models.TextField(null=True, blank=True)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'Review by {self.user}'

    def get_absolute_url(self):
        return reverse('detail-review', kwargs={'book_id': self.book_id})


class FavoriteBook(models.Model):
    book_id = models.CharField(max_length=200, null=True)
    data = models.JSONField(null=True)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'Book ID: {self.book_id}'
