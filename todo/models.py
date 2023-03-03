from django.db import models

# Create your models here.
class Todos(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    status = models.BooleanField()
    date = models.DateTimeField()

    class Meta:
        db_table = 'todos'