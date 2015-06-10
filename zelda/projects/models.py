from django.db import models


class ProjectTypes(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)

class Projects(models.Model):
    type = models.ForeignKey(ProjectTypes)
    test= 'schtroudel'


