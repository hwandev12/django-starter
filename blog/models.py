from django.db import models

class Cards(models.Model):
    
    heading = models.CharField(max_length=200)
    text = models.TextField(max_length=700)
    category = models.ForeignKey("Category", null=True, on_delete=models.SET_NULL)
    
    def __str__(self):
        return self.heading

class Category(models.Model):
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Category"
        
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name


class Andijon(models.Model):
    
    ovqat = models.CharField(max_length=130)
    text = models.TextField(max_length=700)

    def __str__(self):
        return self.ovqat

class Namangan(models.Model):
    
    class Meta:
        verbose_name = "Namangan Qo'shish"
        verbose_name_plural ="Namangan"

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
    
    
class Author(models.Model):
    
    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Author"
        
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=30)
    age = models.IntegerField(default=20)
    
    def __str__(self):
        return self.firstname
    
class Books(models.Model):

    class Meta:
        verbose_name = "Books"
        verbose_name_plural = "Books"
        
    book_name = models.CharField(max_length=60)
    book_date = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.book_name