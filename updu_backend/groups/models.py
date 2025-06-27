from django.db import models

# Create your models here.
class Group(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    members = models.ManyToManyField('users.User', related_name='joined_groups', blank=True)
    created_by = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='created_groups')

    def __str__(self):
        return self.name