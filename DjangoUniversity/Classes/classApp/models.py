from django.db import models


# Create your models here.
class djangoClasses(models.Model):
    title = models.CharField(max_length=60, default='')
    course_number = models.DecimalField(default=0000, max_digits=10000, decimal_places=0)
    instructor_name = models.CharField(max_length=60)
    duration = models.DecimalField(default=000.00, max_digits=10000, decimal_places=2)

    objects = models.Manager()

    def __str__(self):
        return self.title
