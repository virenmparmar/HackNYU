from django.db import models

# Create your models here.


from django.contrib.auth.models import User

class ItemListings(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    photo_path = models.CharField(max_length=200)
    longitutude = models.FloatField()
    latitude = models.FloatField()
    status = models.CharField(max_length=1)
    rating = models.IntegerField()