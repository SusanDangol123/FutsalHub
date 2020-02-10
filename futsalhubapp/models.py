from django.db import models


class User(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password= models.CharField(max_length=60)
    class Meta:
        db_table="user"

class Player(models.Model):
    pid = models.AutoField(auto_created=True, primary_key=True)
    fname = models.CharField(max_length=110)
    lname = models.CharField(max_length=90)
    username = models.CharField(max_length=101)
    email = models.CharField(max_length=60)
    password= models.CharField(max_length=70)
    repassword= models.CharField(max_length=70)

    class Meta:
        db_table="player"

