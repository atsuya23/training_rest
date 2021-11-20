from django.utils import timezone
from django.db import models

MEMO_CATEGORY = [
    ("training", "トレーニング"),
    ("habit", "習慣"),
    ("future", "将来"),
    ("study", "勉強"),
    ("other", "その他"),
]


class Memo(models.Model):
    title = models.CharField(max_length=40)
    memo = models.CharField(max_length=300)
    category = models.CharField(max_length=30, choices=MEMO_CATEGORY)
    created_at = models.DateField(default=timezone.now())

    def __str__(self):
        return self.title
