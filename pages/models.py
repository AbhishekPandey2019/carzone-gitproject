from django.db import models

# Create your models here.
class Team(models.Model):
    first_name = models.CharField(max_length=225)
    last_name= models.CharField(max_length=225)
    desigination = models.CharField(max_length=225)
    photo = models.ImageField(upload_to='photo/%y/%m/%d/')
    facebook_link = models.URLField(max_length=225)
    twitter_link = models.URLField(max_length=225)
    google_plus_link = models.URLField(max_length=225)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name
