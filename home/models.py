from django.db import models

# Create your models here.
class Contact(models.Model):
    sr = models.AutoField(primary_key=True)
    First_Name = models.CharField(max_length=50)
    Last_Name = models.CharField(max_length=50)
    Email = models.CharField(max_length=70)
    Class= models.CharField(max_length=12)
    Section = models.CharField(max_length=5)
    Message = models.TextField()
    DateStamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.First_Name + ' class- ' + self.Class