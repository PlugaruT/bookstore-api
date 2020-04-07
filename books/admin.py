from django.contrib import admin
from .models import Image, Author, Book

admin.site.register(Image)
admin.site.register(Book)
admin.site.register(Author)
