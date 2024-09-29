"""Modelo do banco de dados."""

from datetime import datetime
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Review(models.Model):
    """_summary_

    Args:
        models (_type_): _description_
    """

    user: User = models.ForeignKey(User, on_delete=models.CASCADE)
    game_name: str = models.CharField(max_length=100)
    stars: int = models.IntegerField()
    date_posted: datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str: # pylint: disable=invalid-str-returned
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.game_name
