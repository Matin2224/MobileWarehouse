from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=255, unique=True)
    nationality = models.CharField(max_length=255)

    class META:
        verbose_name = 'brand'
        verbose_name_plural = 'brands'
        ordering = ['name']

    def __str__(self):
        return f"{self.name} brand from {self.nationality}"


class Mobile(models.Model):
    AVAILABILITY = [
        ('available', 'available'),
        ('unavailable', 'unavailable'),
    ]

    brand = models.ForeignKey(Brand, on_delete=models.DO_NOTHING, related_name="mobiles")
    model = models.CharField(max_length=255, unique=True)
    price = models.PositiveIntegerField()
    color = models.CharField(max_length=255)
    screen_size = models.PositiveIntegerField()
    availability_status = models.CharField(max_length=20, choices=AVAILABILITY)
    assembling_country = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'mobile'
        verbose_name_plural = 'mobiles'
        ordering = ['brand', 'price']

    def __str__(self):
        return f"phone: brand: {self.brand.name} - model: {self.model} - price: {self.price} - color: {self.color} -\
         screen size: {self.screen_size} - assembling country: {self.assembling_country}"
