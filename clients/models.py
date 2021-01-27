from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=148)
    description = models.TextField()

class UnLoading(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    details = models.TextField()
    date = models.DateField(auto_now_add=True)
    price = models.PositiveIntegerField()
    alredy_paid = models.PositiveIntegerField(default=0)
