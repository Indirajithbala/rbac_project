from django.db import models

class Role(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Permission(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    roles = models.ManyToManyField(Role)
    permissions = models.ManyToManyField(Permission, blank=True)

    def __str__(self):
        return self.username
