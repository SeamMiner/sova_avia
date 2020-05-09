from django.db import models


class Admin(models.Model):
    login = models.CharField(max_length=25, unique=True)
    password = models.CharField(max_length=25)
    title_company = models.CharField(max_length=50)

    def __str__(self):
        return self.login


class User(models.Model):
    login = models.CharField(max_length=25, unique=True)
    password = models.CharField(max_length=25)
    email = models.CharField(max_length=35)
    phone = models.CharField(max_length=17)
    fio = models.CharField(max_length=100)
    experience = models.PositiveSmallIntegerField()
    specialization = models.CharField(max_length=256, null=True, blank=True)
    admin = models.ForeignKey(Admin, on_delete=models.CASCADE)
    department = models.CharField(max_length=100, null=True, blank=True)
    town = models.CharField(max_length=100, null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.login
