from django.db import models

# Create your models here.
class PythonBlog(models.Model):
    python_title = models.CharField(max_length = 50)
    python_image = models.ImageField(upload_to="images/")
    python_summery = models.CharField(max_length = 100000)

    def __str__(self):
        return self.python_title

class DjangoBlog(models.Model):
    django_title = models.CharField(max_length = 50)
    django_image = models.ImageField(upload_to="images/")
    django_summery = models.CharField(max_length = 100000)

    def __str__(self):
        return self.django_title
