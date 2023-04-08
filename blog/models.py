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

class Namangan(models.Model):
    
    viloyat = models.CharField(max_length=60)
    viloyat_haqida = models.TextField(max_length=700)
    odam_soni = models.IntegerField()
    ortacha_yosh = models.IntegerField()
    tumanlar_soni = models.IntegerField()
    image = models.ImageField(null=True)

    def __str__(self):
        return self.viloyat

class Buxoro(models.Model):
    
    viloyat = models.CharField(max_length=60)
    viloyat_haqida = models.TextField(max_length=700)
    odam_soni = models.IntegerField()
    ortacha_yosh = models.IntegerField()
    tumanlar_soni = models.IntegerField()
    
    def __str__(self):
        return self.viloyat