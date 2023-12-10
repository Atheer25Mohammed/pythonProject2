from django.db import models


class Member(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.IntegerField(default='0553898566')
    joined_date = models.DateField(default='2023-1-2')

    def __str__(self):
        return f"{self.firstname} {self.lastname}"
