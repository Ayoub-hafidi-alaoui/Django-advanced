from django.db import models


# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField()
    bio = models.TextField(max_length=500)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="book_author")
    publish_date = models.DateField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.title


RATE_CHOICES = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
)


class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="review_book")
    reviewer_name = models.CharField(max_length=100)
    review = models.TextField(max_length=500)
    rate = models.IntegerField(choices=RATE_CHOICES)

    def __str__(self):
        return "review " + str(self.book)  + "by " + str(self.reviewer_name)
