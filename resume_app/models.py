from django.db import models


class Res0(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return "%s" %(self.name)

class Res1(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return "%s" %(self.name)

class Pg0(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return "%s" %(self.name)

class Pg1(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return "%s" %(self.name)