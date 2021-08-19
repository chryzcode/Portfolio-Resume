from django.db import models

# Create your models here.
class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    message = models.TextField()

    def __str__ (self):
        return self.name

    def get_absolute_url(self):
        return reverse('the_view')