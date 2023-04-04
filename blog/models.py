from django.db import models

class Cards(models.Model):
    
    heading = models.CharField(max_length=200)
    text = models.TextField(max_length=700)
    
    def __str__(self):
        return self.heading

class Andijon(models.Model):
    
    ovqat = models.CharField(max_length=130)
    text = models.TextField(max_length=700)
    
    def __str__(self):
        return self.ovqat
    
