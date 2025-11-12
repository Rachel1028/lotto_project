from django.db import models
from django.contrib.auth.models import User
import random

class LottoTicket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    numbers = models.CharField(max_length=30)
    is_winner = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.numbers}'

    @staticmethod
    def generate_auto_numbers():
        nums = sorted(random.sample(range(1, 46), 6))
        return ', '.join(map(str, nums))
