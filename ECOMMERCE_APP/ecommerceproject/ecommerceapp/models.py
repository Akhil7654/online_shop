from django.db import models
from django.urls import reverse
# Create your models here.

class Category(models.Model):
    cname=models.CharField(max_length=250,unique=True)
    cimage=models.ImageField(upload_to="category",blank=True)
    cdesc=models.TextField(blank=True)
    slug=models.SlugField(max_length=250,unique=True)

    class Meta:
        ordering=('cname',)
        verbose_name="category"
        verbose_name_plural="categories"

    def get_url(self):
        return reverse('ecommerceapp:products_category',args=[self.slug])

    def __str__(self):
        return self.cname

class Product(models.Model):
    pname=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(unique=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    pdesc=models.TextField(blank=True)
    pimage=models.ImageField(upload_to="products",blank=True)
    pprice=models.DecimalField(max_digits=10,decimal_places=2)
    pcreate=models.DateTimeField(auto_now_add=True)
    pstock=models.IntegerField()
    pavailable=models.BooleanField(default=True)
    pupdate=models.DateTimeField(auto_now=True)

    def get_url(self):
        return reverse('ecommerceapp:product_category_detail',args=[self.category.slug,self.slug])


    class Meta:
        ordering=('pname',)
        verbose_name="product"
        verbose_name_plural="products"

    def __str__(self):
        return self.pname

