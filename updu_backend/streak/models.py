from django.db import models
# Create your models here.

class Streak(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    group_id = models.IntegerField()
    start_date = models.DateField()
    currrent_streak = models.IntegerField(default=0)
