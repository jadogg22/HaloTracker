from django.db import models
from django.forms.models import model_to_dict


# Create your models here.

class GameStats(models.Model):
    gamertag = models.CharField(max_length=100)
    kills = models.IntegerField()
    deaths = models.IntegerField()
    kd_ratio = models.FloatField()
    assists = models.IntegerField() 
    headshots = models.IntegerField()
    accuracy = models.FloatField()
    damage_dealt = models.IntegerField()
    damage_taken = models.IntegerField()
    timeScraped = models.DateTimeField(auto_now_add=True)

# def get_latest_stats(gamertag):
#     latest_stats = GameStats.objects.filter(
#            gamertag=gamertag
#         ).order_by('-timeScraped').first()
    

#     return model_to_dict(latest_stats)

    def __str__(self):
        return self.gamertag
