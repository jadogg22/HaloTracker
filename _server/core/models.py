from django.db import models
from django.forms.models import model_to_dict
from django.utils import timezone
from datetime import datetime


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

    @classmethod
    def create_from_dict(cls, stats_dict):
        return cls(
            gamertag=stats_dict["gamertag"],
            kills=int(stats_dict["kills"].replace(",", "")),
            deaths=int(stats_dict["deaths"].replace(",", "")),
            kd_ratio=float(stats_dict["K/D"]),
            assists=int(stats_dict["assists"].replace(",", "")),
            headshots=int(stats_dict["headshots"].replace(",", "")),
            accuracy=float(stats_dict["accuracy"].replace("%", "")),
            damage_dealt=int(stats_dict["damageDealt"].replace(",", "")),
            damage_taken=int(stats_dict["damageTaken"].replace(",", "")),
        )
    
    def to_dict(self):
        return {
            'gamertag': self.gamertag,
            'kills': self.kills,
            'deaths': self.deaths,
            'kd_ratio': self.kd_ratio,
            'assists': self.assists,
            'headshots': self.headshots,
            'accuracy': self.accuracy,
            'damage_dealt': self.damage_dealt,
            'damage_taken': self.damage_taken,
            'timeScraped': self.timeScraped.strftime('%Y-%m-%d %H:%M:%S'),  # Format the datetime as needed
        }
    
    def get_stats_by_username(username):
        # filter by gamertag and return the first one.
        stats = GameStats.objects.filter(gamertag=username).order_by('-timeScraped').first()

        return stats
        
    def isRecent(self):
        # The oldest data to retrieve in the database
        timeDelay = timezone.timedelta(hours=3)

        #convert to datetime

        now = timezone.now()
        isOldEnough = now - timeDelay

        return isOldEnough <= self.timeScraped <= now



    def __str__(self):
        return self.gamertag
