from django.db import models
from django.contrib.auth.models import User


class Client(models.Model):
    name = models.CharField(max_length=148)
    description = models.TextField()

    def __str__(self):
        return '{}'.format(self.name)


class UnLoading(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    details = models.TextField(default='')
    date = models.DateField(auto_now_add=True)
    price = models.PositiveIntegerField()
    alredy_paid = models.PositiveIntegerField(default=0)
    workers = models.ManyToManyField(User)

    def __str__(self):
        return '{} {}, Цена: {}, Заплачено: {}'.format(self.client.name, self.date, self.price, self.alredy_paid)