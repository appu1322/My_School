from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Physics tut and Comments
class Physic(models.Model):
    sr = models.AutoField(primary_key=True)
    slug = models.CharField(max_length=100)
    title = models.CharField(max_length=500, default='')
    desc = models.CharField(max_length=5000, default='')
    videoFile = models.FileField(upload_to='tut11/physic/', verbose_name='')

    def __str__(self):
        return self.title

class PhysicComment(models.Model):
    sr = models.AutoField(primary_key=True)
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tut = models.ForeignKey(Physic, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE , null=True)
    datestamp = models.DateTimeField(default=now)

    def __str__(self):
        return self.comment[0:13] + "... by " + self.user.username


# chemistry tut and comments
class Chemistry(models.Model):
    sr = models.AutoField(primary_key=True)
    slug = models.CharField(max_length=100)
    title = models.CharField(max_length=500, default='')
    desc = models.CharField(max_length=5000, default='')
    videoFile = models.FileField(upload_to='tut11/chemistry/', verbose_name='')

    def __str__(self):
        return self.title

class ChemistryComment(models.Model):
    sr = models.AutoField(primary_key=True)
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tut = models.ForeignKey(Chemistry, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE , null=True)
    datestamp = models.DateTimeField(default=now)

    def __str__(self):
        return self.comment[0:13] + "... by " + self.user.username


# math tut and comments
class Math(models.Model):
    sr = models.AutoField(primary_key=True)
    slug = models.CharField(max_length=100)
    title = models.CharField(max_length=500, default='')
    desc = models.CharField(max_length=5000, default='')
    videoFile = models.FileField(upload_to='tut11/math/', verbose_name='')

    def __str__(self):
        return self.title

class MathComment(models.Model):
    sr = models.AutoField(primary_key=True)
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tut = models.ForeignKey(Math, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE , null=True)
    datestamp = models.DateTimeField(default=now)

    def __str__(self):
        return self.comment[0:13] + "... by " + self.user.username