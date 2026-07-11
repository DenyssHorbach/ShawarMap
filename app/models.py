from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Point(models.Model):
    name = models.CharField(max_length=50, verbose_name='Restaurant name')
    address = models.CharField(max_length=100, verbose_name='Address')
    description = models.TextField(verbose_name='Description')
    phone_number = models.CharField(max_length=20, verbose_name='Phone number')
    is_active = models.BooleanField(default=True, verbose_name='Is active?')
    mail_address = models.EmailField(verbose_name='Mail address')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated at')
    latitude = models.DecimalField(max_digits=9, decimal_places=6, verbose_name='Latitude',
                                   null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, verbose_name='Longitude',
                                    null=True, blank=True)
    image = models.ImageField(upload_to='images/', verbose_name='Image')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Restaurant"
        verbose_name_plural = "Restaurants"

class Review(models.Model):
    point = models.ForeignKey(Point, on_delete=models.CASCADE, related_name='Review')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='Review',)
    rating = models.PositiveSmallIntegerField(verbose_name='Rating',
                                               validators=[MinValueValidator(1), MaxValueValidator(5)])
    text = models.TextField(verbose_name='Review', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')

    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Reviews"
        unique_together = ('point', 'user')

    def __str__(self):
        return f"Review by {self.user} for {self.point.name} ({self.rating}★)"

class PointImages(models.Model):
    point = models.ForeignKey(Point, on_delete=models.CASCADE, related_name='Images')
    images = models.ImageField(upload_to='images/', verbose_name='Image')
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name='Uploaded at')
