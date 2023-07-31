from django.db import models

# Create your models here.
class MotivationQuote(models.Model):
    id = models.AutoField(primary_key=True)
    quote = models.CharField(max_length=255)
    author = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.id}: {self.quote} - {self.author}"

