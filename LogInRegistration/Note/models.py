from django.db import models
from django.contrib.auth.models import User

class Notes(models.Model):
    """
    This represents the table of the database provided in the credentials. 
    It provides the note details.
    """
    user_note = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()