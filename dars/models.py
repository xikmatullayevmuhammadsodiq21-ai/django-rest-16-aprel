from django.db import models

# Create your models here.


class Category(models.Model):
    tittle = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.tittle}"
    


class Product(models.Model):
    tittle = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.RESTRICT)
    price = models.IntegerField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.tittle}"






