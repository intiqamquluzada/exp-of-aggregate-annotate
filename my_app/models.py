from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


# class Category(MPTTModel):
#     name = models.CharField(max_length=50, unique=True)
#     parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
#
#     class MPTTMeta:
#         order_insertion_by = ['name']
#
#     def __str__(self):
#         if self.parent:
#             return f"{self.parent}-->{self.name}"
#         return self.name


class ProductMaterials(models.Model):
    name = models.CharField(max_length=255, verbose_name="Name")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("name", )
        verbose_name = "Material"
        verbose_name_plural = "Materials"


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="Name of product")
    price = models.FloatField(verbose_name="Price of product")
    count = models.IntegerField(verbose_name="Count of product")
    color = models.CharField(max_length=255, verbose_name="Color of product")
    material = models.ForeignKey(ProductMaterials, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("name",)
        verbose_name = "Product"
        verbose_name_plural = "Products"


