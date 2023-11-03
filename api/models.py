from django.db import models


class Person(models.Model):
    username = models.CharField(max_length=100)
    telegram_id = models.CharField(max_length=50, unique=True)


class House(models.Model):
    house_name = models.CharField(max_length=100)
    members = models.ManyToManyField(Person, related_name='houses')
    owner = models.ForeignKey(Person, related_name='owned_houses', on_delete=models.CASCADE)


class Expense(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    date = models.DateField()
    buyer = models.ForeignKey(Person, on_delete=models.CASCADE)
    # receipt_image = models.ImageField(upload_to='receipts/', blank=True, null=True)


class Settlement(models.Model):
    payer = models.ForeignKey(Person, related_name='payer_settlements', on_delete=models.CASCADE)
    recipient = models.ForeignKey(Person, related_name='recipient_settlements', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

