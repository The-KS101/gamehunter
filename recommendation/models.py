from django.db import models
# Create your models here.
class Games(models.Model):
    name = models.CharField(max_length=50)
    platform = models.CharField(max_length=50)
    release_date = models.DateField()
    meta_score = models.IntegerField()
    gameDesc = models.CharField(max_length=10000)
    user_score = models.FloatField()
    age_rating = models.CharField(max_length=50)
    Devs = models.CharField(max_length=50)
    Genres = models.CharField(max_length=50)
    weighed_score = models.FloatField()
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name