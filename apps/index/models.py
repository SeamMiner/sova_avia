from django.db import models


class User(models.Model):
    login = models.CharField(max_length=25, unique=True)
    password = models.CharField(max_length=25)
    # photo = models.FileField(upload_to='uploads/')
    phone = models.CharField(max_length=17)
    fio = models.CharField(max_length=100)
    experience = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.login


class Admin(models.Model):
    login = models.CharField(max_length=25, unique=True)
    password = models.CharField(max_length=25)

    def __str__(self):
        return self.login
