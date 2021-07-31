from django.db import models

class VocabWord(models.Model):
    word = models.CharField(max_length=30, primary_key=True)
    definition = models.CharField(max_length=300)
    word_class = models.CharField(max_length=30, default="verb")
    creation_date = models.DateTimeField(auto_now_add=True)
    last_seen = models.DateTimeField(auto_now=True)
    seen_count = models.IntegerField()
    correct_count = models.IntegerField()

    def __str__(self):
        return f"{self.word} ({self.word_class})"