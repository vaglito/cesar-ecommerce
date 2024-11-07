from django.db import models
from django.template.defaultfilters import slugify
import uuid

# Create your models here.
class Product(models.Model):
    """
    Represents a product available for sale

    Attr:
        id (UUIDField): identification unique for product, generated automatically.
        title (CharField): The product title, unique and limits 255 characters
        category (CharField): The product category.
        price (FloatField): The product price.
        slug (SlugField): Single field that is automatically generated from the title. Commonly used in friendly URLs.

    Methods:
        save(): Overwrite the method `save` for automatically generated field `slug` from the title.
        __str__(): Returns the title product 
    """
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    title = models.CharField("Titulo", max_length=255, unique=True)
    category = models.CharField("Categoria", max_length=50)
    price = models.FloatField()
    slug = models.SlugField(unique=True, max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        db_table = "productos"
        db_table_comment = "Productos para vender"
    
    def save(self, *args, **kwargs):
        """
        Generates the slug from the product title
        
        Overwrite the methods `save`
        """
        if self.title:
            self.slug = slugify(self.title)

        super(Product, self).save(*args, **kwargs)
    
    def __str__(self):
        """
        returns the title of the product

        Returns:
            str: title
        """
        return self.title
