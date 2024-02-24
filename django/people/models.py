from django.db import models

class User(models.Model):
    username = models.CharField(max_length=200)

    def __str__(self):
        """
        String to represent the User object (in Admin site etc.)
        """
        return self.username


    class Meta:
        ordering = ('username',)
