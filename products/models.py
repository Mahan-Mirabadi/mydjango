from django.db import models
from django.utils.text import slugify
from django.core.validators import MinValueValidator,MaxValueValidator

# Create your models here.
class ProductInfo(models.Model):
    color=models.CharField(max_length=100, verbose_name='رنگ')
    size=models.IntegerField(verbose_name='سایز')
    def __str__(self):
        return f'{self.color}----{self.size}'
    class Meta:
        verbose_name='اطلاعات'
        verbose_name_plural='لیست اطلاعات'
class ProductCategory(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان') 
    slug=models.SlugField(default='',null=False,db_index=True, verbose_name='اسلاگ')
    def __str__(self):
        return f'{self.title}'
    class Meta:
        verbose_name='دسته بندی'
        verbose_name_plural='لیست دسته بندی ها'
class Product(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان') 
    category=models.ForeignKey(ProductCategory,on_delete=models.CASCADE,null=True,blank=True,related_name='category')
    info=models.OneToOneField(ProductInfo,on_delete=models.CASCADE,null=True,blank=True,related_name='Product_Info',verbose_name='اطلاعات کالا')
    price=models.IntegerField(verbose_name='قیمت')
    description=models.TextField(verbose_name='توضیحات')
    is_active=models.BooleanField(default=True, verbose_name='فعالیت')
    slug=models.SlugField(default='',null=False,db_index=True, verbose_name='اسلاگ')
    ratings=models.IntegerField(default=0,validators=[MaxValueValidator(5),MinValueValidator(0)], verbose_name='نمره')
    def save(self, *args, **kwargs):
        self.slug=slugify(self.title)
        super().save(*args, **kwargs)
    def __str__(self):
        return f'{self.title}----{self.price}'
    class Meta:
        verbose_name='محصول'
        verbose_name_plural='محصولات'



