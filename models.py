from django.db import models

# Create your models here.
class Task(models.Model):
    index=models.BigIntegerField(primary_key=True)
    id = models.BigIntegerField()
    Season = models.TextField(blank=True,max_length=50)
    city = models.TextField(max_length=50)
    date = models.TextField(max_length=150,unique=True)
    team1 = models.TextField()
    team2 = models.TextField()
    toss_winner = models.TextField()
    toss_decision = models.TextField()
    result = models.TextField()
    dl_applied = models.BigIntegerField()
    winner = models.TextField()
    win_by_runs = models.BigIntegerField()
    win_by_wickets= models.BigIntegerField()
    player_of_match=models.TextField()
    venue=models.TextField(max_length=50)
    umpire1=models.TextField(blank=True)
    umpire2=models.TextField(blank=True)
    umpire3=models.TextField(blank=True)
    def __str__(self):
        return self.date