from django.db import models


class Topic(models.Model):
    """a topic the user is learning about"""

    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """return str representation of model"""
        return self.text
