from django.db import models



class Book(models.Model):
    AUTHOR_CHOICE = (
        ('Pushkin', 'Pushkin'),
        ('Lermantov', 'Lermantov'),
        ('Esenin', 'Esenin'),
        ('Gogol', 'Gogol')
    )
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='')
    pages = models.IntegerField(null=True)
    author = models.CharField(choices=AUTHOR_CHOICE, max_length=100, null=True)
    date_books = models.DateField(null=True)























