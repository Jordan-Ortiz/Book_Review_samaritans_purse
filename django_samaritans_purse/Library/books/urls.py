from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('create_review/', create_review, name='create-review'),
    path('details/<str:id>', book_details, name='detail-review'),
    path('create_favortie/<str:id>', create_favorite, name='add-favorite'),
    path('review_detail/<int:pk>', BookDetailView.as_view(), name='review-detail'),
    path('review/<str:id>', CreateBookReview.as_view(), name='review'),
    path('favorite_list/', FavoriteBookList.as_view(), name='favorite_list'),
    path('review_list/', ListReviews.as_view(), name='review_list'),
    path('my_review_list/', MyReviewList.as_view(), name='review_list_user'),
    path('delete_review/<int:pk>', DeleteReview.as_view(), name='delete-review'),
    path('update_review/<int:pk>', UpdateReview.as_view(), name='update-review'),
]