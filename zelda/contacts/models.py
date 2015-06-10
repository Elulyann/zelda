from django.db import models

# Create your models here.
class Title(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

class Categorie(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Contact(models.Model):
    title = models.ForeignKey(Title, null=True)
    last_name = models.CharField(max_length=250)
    first_name = models.CharField(max_length=250)
    zip_code = models.CharField(max_length=5, default='')
    email = models.CharField(max_length=250, null=True)
    categories = models.ManyToManyField(Categorie)
