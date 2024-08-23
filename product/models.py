from django.db import models
from django.contrib.auth.models import User
from django.db.models import JSONField


class ProductCategory(models.Model):
    name = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    published = models.BooleanField(default=False)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    model_number = models.CharField(max_length=100, blank=True, null=True)
    stock = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    featured_image = models.ImageField(upload_to='product_images/')
    description = models.TextField(blank=True, null=True)
    specifications = JSONField(blank=True, null=True,)  # To store additional specific attributes
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    brand = models.CharField(max_length=20, blank="", null=True)
    # slug

    def __str__(self):
        return self.name

class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    image = models.ImageField(upload_to='product_images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Image for {self.product.name}"

class ProductOffer(models.Model):
    product = models.OneToOneField(Product, related_name='offer', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    price_after_offer = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    discount_percent = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f"Offer for {self.product.name}"

class ProductLog(models.Model):
    product = models.ForeignKey(Product, related_name='log', on_delete=models.CASCADE)
    logger = models.ForeignKey(User, on_delete=models.CASCADE)
    ip = models.GenericIPAddressField()
    mac = models.CharField(max_length=17)
    browser_agent = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Log for {self.product.name} by {self.logger.username}"

class ProductViewer(models.Model):
    product = models.ForeignKey(Product, related_name='viewer', on_delete=models.CASCADE)
    ip = models.GenericIPAddressField()
    mac = models.CharField(max_length=17)
    browser_agent = models.CharField(max_length=255)
    viewed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Viewer log for {self.product.name}"

class Location (models.Model):
    name=models.CharField(max_length=22)
    details=models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Location :{self.name}"

class ProductLocation(models.Model):
    product = models.ForeignKey(Product, related_name='product', on_delete=models.CASCADE)
    location = models.ForeignKey(Location, related_name="location", on_delete=models.CASCADE)
    note = models.CharField(max_length=255,blank=True,null=True)

    def __str__(self):
        return f"location prodcut for {self.product.name}"

class FeaturedProduct(models.Model):
    product = models.OneToOneField(Product, related_name='featured_product', on_delete=models.CASCADE)
    active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title= models.CharField(max_length= 25)
    short_description=  models.CharField(max_length=50)

class OfferProductNews(models.Model):
    title= models.CharField(max_length=500)
    description =models.TextField(max_length=2000)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active= models.BooleanField(default=False)





class TrendingProduct(models.Model):
    product = models.OneToOneField(Product, related_name='trending_product', on_delete=models.CASCADE)
    active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class MostSoldProduct(models.Model):
    product = models.OneToOneField(Product, related_name='mostsold_product', on_delete=models.CASCADE)
    active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

