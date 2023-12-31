from django.contrib import admin

from .models import Book, Review, Author

# Register your models here.

admin.site.register([Book, Review, Author])
