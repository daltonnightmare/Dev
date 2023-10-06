from django.contrib.auth.models import User
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='catégorie')

    class Meta:
        ordering = ('name',)
        verbose_name = 'Categorie'
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name

class Item(models.Model):
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE, verbose_name='catégorie')
    name = models.CharField(max_length=255, verbose_name='nom')
    description = models.TextField(blank=True, null=True)
    price = models.FloatField(verbose_name='prix')
    image = models.ImageField(upload_to='item_images', blank=True, null=True)
    is_sold = models.BooleanField(default=False, verbose_name='en rupture de stock')
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE, verbose_name='créer par')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='créer le')
    
    def __str__(self):
        return self.name