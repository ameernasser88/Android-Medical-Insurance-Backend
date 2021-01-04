from django.db import models


class Hospital(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField(max_length=1000, null=True)
    location = models.TextField(max_length=1000, null=True)
    telephone_number = models.TextField(max_length=100, null=True)
    website = models.TextField(max_length=1000, null=True)

    def __str__(self):
        return self.name


class Clinic(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField(max_length=1000, null=True)
    specialization = models.TextField(max_length=1000, null=True)
    location = models.TextField(max_length=1000, null=True)
    telephone_number = models.TextField(max_length=1000, null=True)
    website = models.TextField(max_length=1000, null=True)

    def __str__(self):
        return self.name
