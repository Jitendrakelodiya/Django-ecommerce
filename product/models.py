from django.db import models
from django.utils.text import slugify
from autoslug import AutoSlugField

# Create your models here.


class Elec_Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    product_price = models.IntegerField(default=0)
    product_desc = models.CharField(max_length=500)
    pub_date = models.DateField()
    product_image = models.ImageField(upload_to="static/images", default="")
    slug = models.SlugField(unique=True, blank=True, null=True)

    # elec_slug = AutoSlugField(populate_from='product_name',unique=True,null=True,default=None)

    def __str__(self):
        return self.product_name
    
class Cloth_Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    product_price = models.IntegerField(default=0)
    product_desc = models.CharField(max_length=500)
    pub_date = models.DateField()
    product_image = models.ImageField(upload_to="static/images", default="")
    slug = models.SlugField(unique=True, blank=True, null=True)

    # elec_slug = AutoSlugField(populate_from='product_name',unique=True,null=True,default=None)

    def __str__(self):
        return self.product_name  

class H_K_Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    product_price = models.IntegerField(default=0)
    product_desc = models.CharField(max_length=500)
    pub_date = models.DateField()
    product_image = models.ImageField(upload_to="static/images", default="")
    slug = models.SlugField(unique=True, blank=True, null=True)

    # elec_slug = AutoSlugField(populate_from='product_name',unique=True,null=True,default=None)

    def __str__(self):
        return self.product_name
    
class Groceries_Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    product_price = models.IntegerField(default=0)
    product_desc = models.CharField(max_length=500)
    pub_date = models.DateField()
    product_image = models.ImageField(upload_to="static/images", default="")
    slug = models.SlugField(unique=True, blank=True, null=True)

    # elec_slug = AutoSlugField(populate_from='product_name',unique=True,null=True,default=None)

    def __str__(self):
        return self.product_name

# class Category_type(models.Model):
#     status = (
#         ('True', 'True'),
#         ('False', 'False'),
#     )
#     Catg_Name =models.ForeignKey('self',blank=True,null=True,related_name='children',on_delete=models.CASCADE)
#     title = models.CharField(max_length=100)
#     description = models.CharField(max_length=500)
#     image = models.ImageField(blank=True,upload_to="static/images")
#     price = models.IntegerField(default=0)
#     status = models.CharField(max_length=20, choices=status)
#     slug = models.SlugField()
#     create_at =models.DateTimeField(auto_now_add=True)
#     update_at =models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.title
    

# class Product_type(models.Model):
#     status = (
#         ('True', 'True'),
#         ('False', 'False'),
#     )
#     Catg_Name =models.ForeignKey(Category_type,on_delete=models.CASCADE)
#     title = models.CharField(max_length=100)
#     description = models.CharField(max_length=500)
#     image = models.ImageField(blank=True,upload_to="static/images")
#     price = models.IntegerField(default=0)
#     status = models.CharField(max_length=20, choices=status)
#     slug = models.SlugField()
#     create_at =models.DateTimeField(auto_now_add=True)
#     update_at =models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.title
    
class Category_shop(models.Model):
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.category
    
class Product_shop(models.Model):
    category = models.ForeignKey(Category_shop, on_delete=models.CASCADE)
    product_name = models.CharField( max_length=50)
    product_price = models.CharField(max_length=20)
    product_desc = models.CharField(max_length=500)
    pub_date = models.DateField()
    product_image = models.ImageField(upload_to="static/images", default="")
    mark = models.BooleanField(default=False)
    elec_slug = AutoSlugField(populate_from='product_name',unique=True,null=True,default=None)


    def __str__(self):
        return self.product_name