from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    lecturer = models.CharField(max_length=100, blank=False)
    date_added = models.DateField(auto_now_add=True)
    description = models.TextField()

    def __str__(self):
        return self.name