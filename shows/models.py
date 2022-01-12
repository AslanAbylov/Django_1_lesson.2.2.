from django.db import models



class TVShow(models.Model):
    GANER_CHOICE = (
        ('Detective', 'Detective'),
        ('Comedy', 'Comedy'),
        ('Drama', 'Drama'),
        ('Horror', 'Horror'),
        ('Romantic', 'Romantic'),
        ('Anime', 'Anime')
    )
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='')
    quantity = models.ImageField()
    genre = models.CharField(choices=GANER_CHOICE, max_length=100)
    date_filmed = models.DateField



