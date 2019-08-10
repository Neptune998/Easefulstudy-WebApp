from django.db import models


class Login(models.Model):
    Username = models.CharField(max_length=20)
    password = models.CharField(max_length=10)


