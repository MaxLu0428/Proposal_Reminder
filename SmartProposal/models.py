from django.db import models

# Create your models here.
class Proposal(models.Model):
    Name = models.CharField(max_length=50)
    Description = models.TextField()
    Action = models.CharField(max_length=50)
    Document_Number = models.CharField(max_length=50)

    def __str__(self) -> str:
        return  "{}-{}".format(self.Document_Number,self.Name)
    
class vDRM(models.Model):
    Name = models.CharField(max_length=50)
    Description = models.TextField()
    Document_Number = models.CharField(max_length=50)

    def __str__(self) -> str:
        return  "{}-{}".format(self.Document_Number,self.Name)
    

