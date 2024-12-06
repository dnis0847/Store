from django.contrib import admin
from django.db import models
from django.utils import timezone

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail

# Товары в магазине
class Product(models.Model):
    
    class Available(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(quantity__gt=0)
    
    
    title = models.CharField(max_length=255, verbose_name='Название товара')
    article = models.CharField(max_length=255, verbose_name='Артикул')
    brand = models.CharField(max_length=255, verbose_name='Бренд-производитель')
    description = models.TextField(verbose_name='Описание товара')
    rating = models.DecimalField(max_digits=3, decimal_places=2, verbose_name='Оценка товара')
    quantity = models.IntegerField(verbose_name='Количество товара на складе')
    publish = models.DateTimeField(default=timezone.now, verbose_name='Дата публикации', db_index=True)

    objects = models.Manager()
    available_objects = Available()
    
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['-publish', 'title']
        
    def __str__(self):
        return f"{self.title}"
    
    def get_absolute_url(self):
        return f"/product/{self.id}/"

    
