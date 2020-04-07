from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('register', views.register, name='register'),
    path('images', views.images, name='images'),
    path('authors', views.authors, name='authors'),
    path('books', views.books, name='books'),
    path('books/<int:author_id>', views.author_books, name="books-for-author"),
    url(r'^auth/', views.CustomAuthToken.as_view()),
]