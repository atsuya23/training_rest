from django.utils import timezone
from django.contrib import admin
from django.db import models

TRAINING_PLACE = [
    ("home", "Home"),
    ("zym", 'Zym'),
    ('others', 'Others'),
]

EVALUATION_PLACE = [
    ("excellent", '☆'),
    ("good", '◎'),
    ("normal", '〇'),
    ('bad', '×'),
]


class Training(models.Model):
    review = models.CharField(max_length=100, null=True, blank=True)
    evaluation = models.CharField(max_length=10,
                                  choices=EVALUATION_PLACE,
                                  default="good")
    place = models.CharField("Place",
                             max_length=10,
                             choices=TRAINING_PLACE,
                             default="home")
    created_at = models.DateField("Date", default=timezone.now())
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.created_at)


TRAINING_CHOICES = [
    ('bench_press', 'ベンチプレス'),
    ("incline_bench_press", 'インクラインベンチプレス'),
    ('decline_bench_press', 'デクラインベンチプレス'),
    ("dumbbell_press", "ダンベルプレス"),
    ('shoulder_press', 'ショルダープレス'),
    ('lat_pull_down', 'ラットプルダウン'),
    ('chinning', 'チンニング'),
    ('push-up', '腕立て'),
    ('over_head_press', 'トライセプスエクステンション'),
    ('side_rise', 'サイドレイズ'),
    ('arm_curl', 'アームカール'),
    ('dips', 'ディップス'),
    ('kick_back', 'キックバック'),
    ('arm_variations', '上腕総合'),
    ('something_new', '新種目'),
]


class Content(models.Model):
    id_training = models.ForeignKey(Training, on_delete=models.CASCADE, related_name="id_training")
    training_type = models.CharField(max_length=40, choices=TRAINING_CHOICES)
    weight = models.PositiveIntegerField("Weight[Kg]", default=70)
    set1 = models.PositiveIntegerField(default=10)
    set2 = models.PositiveIntegerField(default=9, null=True, blank=True)
    set3 = models.PositiveIntegerField(default=8, null=True, blank=True)

    def __str__(self):
        return f"{self.training_type} : {self.weight}Kg"

    @admin.display(
        boolean=True,
        ordering='created_at',
        description='enough weight?',
    )
    def weight_is_enough(self):
        if self.training_type == "bench_press" and \
                (self.set1 >= 15 or (self.set2 and self.set2 >= 12) or (self.set3 and self.set3 >= 10)):
            return False
        else:
            return True

    @admin.display(
        ordering='id_training',
        description='weight amounts',
    )
    def weight_amounts(self):
        if self.weight:
            if self.set1 and self.set2 and self.set3:
                return f"{self.weight}Kg * ( {self.set1} + {self.set2} + {self.set3} )"
            elif self.set1 and self.set2:
                return f"{self.weight}Kg * ( {self.set1} + {self.set2} )"
            elif self.set1:
                return f"{self.weight}Kg * {self.set1}"

        elif not self.weight:
            if self.set1 and self.set2 and self.set3:
                return f"prudence ( {self.set1} + {self.set2} + {self.set3} )"
            elif self.set1 and self.set2:
                return f"prudence ( {self.set1} + {self.set2} )"
            elif self.set1:
                return f"prudence {self.set1}"


class TrainingType(models.Model):
    type = models.CharField(max_length=30, unique=True)

    # goal_amount = models.PositiveIntegerField(default=0, null=True, blank=True)
    # main_part = models.CharField(max_length=100, default="", null=True, blank=True)

    def __str__(self):
        return self.type


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

