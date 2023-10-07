from django.db import models
from django.contrib.auth.models import User

# account


class account(models.Model):
    x = [
        ('doctor', 'doctor'), ('patient', 'patient')
    ]
    y = [
        ('cash', 'cash'), ('paypal', 'paypal'), ('visa', 'visa')
    ]
    user = models.OneToOneField(
        User, unique=True, null=True, blank=True, on_delete=models.CASCADE)
    email = models.EmailField(null=True, blank=True)
    fullName = models.CharField(max_length=50, blank=True, null=True)
    gender = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    DateOfBirth = models.CharField(max_length=50, blank=True, null=True)
    DocOrPat = models.TextField(choices=x, blank=True)
    specialList = models.CharField(max_length=50, blank=True, null=True)
    yearOfExp = models.IntegerField(blank=True, default=1)
    payMethod = models.TextField(choices=y, blank=True)
    payEmail = models.EmailField(blank=True)
    proPic = models.FileField(upload_to='media', blank=True)
    price = models.FloatField(blank=True, null=True)

    def __str__(self):
        return str(self.user.username)
# draft task in home


class draft(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    thought = models.CharField(max_length=100)

    def __str__(self):
        return self.title
