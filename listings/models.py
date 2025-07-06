from django.db import models
from django.contrib.auth.models import User

class Listing(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="properties")
    title = models.CharField(max_length=150)
    description = models.TextField()
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    area = models.PositiveIntegerField(help_text="Площадь в м²")
    rooms = models.PositiveSmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    PROPERTY_TYPES = [
        ('apartment', 'Квартира'),
        ('house', 'Дом'),
        ('commercial', 'Коммерческая недвижимость'),
        ('land', 'Участок'),
    ]
    property_type = models.CharField(max_length=20, choices=PROPERTY_TYPES)

    def __str__(self):
        return f"{self.title} ({self.city})"

class YourModel(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    city = models.CharField(max_length=50)

class Comment(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Комментарий от {self.name} к {self.listing.title}"
