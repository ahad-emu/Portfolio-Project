from django.db import models

# Create your models here.
class Portfolio(models.Model):
    image = models.ImageField(upload_to = "images/")
    summery = models.CharField(max_length = 100)

    def shortSummery(self):
        return self.summery[:50]
