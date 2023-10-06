from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.urls import reverse





class Brand(models.Model):
    title = models.CharField(max_length=255, verbose_name='عنوان برند')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'برند'
        verbose_name_plural = 'برندها'




def special_brand_image_path(instance, filename):
    date_str = datetime.now().strftime('%Y/%m/%d')
    unique_filename = f'topkalaTemplate/special_brand_images/{date_str}/{filename}'
    return unique_filename


class SpecialBrand(models.Model):
    name = models.CharField(max_length=255, verbose_name='نام برند')
    logo = models.ImageField(upload_to=special_brand_image_path, verbose_name='لوگو برند')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'برند ویژه'
        verbose_name_plural = 'برندهای ویژه'


class Category(models.Model):
    title = models.CharField(max_length=255)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    url = models.URLField(blank=True ,null=True)

    def __str__(self):
        return self.title



def product_image_path(instance, filename):
    date_str = datetime.now().strftime('%Y/%m/%d')
    unique_filename = f'topkalaTemplate/product_images/{date_str}/{filename}'
    return unique_filename


class Product(models.Model):
    title = models.CharField(max_length=255, verbose_name='عنوان محصول')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='دسته‌بندی')
    # image = models.ImageField(upload_to=product_image_path, verbose_name='تصویر محصول')
    old_price = models.IntegerField(verbose_name='قیمت قبلی')
    new_price = models.IntegerField(verbose_name='قیمت جدید')
    discount_percent = models.PositiveIntegerField(verbose_name='درصد تخفیف')
    description = models.TextField(verbose_name='توضیحات محصول')
    countdown_date = models.DateTimeField(null=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name='برند',null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'
    
    def get_absolute_url(self):
        # ایجاد URL محصول
        return reverse('topkalaTemplate:single-product', args=[str(self.id)])

    def get_twitter_share_url(self):
        # تابع برای ایجاد لینک اشتراک‌گذاری در توییتر
        product_url = self.get_absolute_url()
        twitter_share_url = f'https://twitter.com/intent/tweet?url={product_url}&text={self.title}'
        return twitter_share_url

    def get_facebook_share_url(self):
        # تابع برای ایجاد لینک اشتراک‌گذاری در فیسبوک
        product_url = self.get_absolute_url()
        facebook_share_url = f'https://www.facebook.com/sharer/sharer.php?u={product_url}'
        return facebook_share_url

    def get_google_plus_share_url(self):
        # تابع برای ایجاد لینک اشتراک‌گذاری در گوگل پلاس
        product_url = self.get_absolute_url()
        google_plus_share_url = f'https://plus.google.com/share?url={product_url}'
        return google_plus_share_url
    



class FavoriteProduct(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'product')


class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE, verbose_name='محصول')
    image = models.ImageField(upload_to=product_image_path, verbose_name='تصویر محصول')

    def __str__(self):
        return self.product.title + ' - Image'

    class Meta:
        verbose_name = 'تصویر محصول'
        verbose_name_plural = 'تصاویر محصولات'



def slider_image_path(instance, filename):
    date_str = datetime.now().strftime('%Y/%m/%d')
    unique_filename = f'topkalaTemplate/slider_images/{date_str}/{filename}'
    return unique_filename



class SliderImage(models.Model):
    image = models.ImageField(upload_to=slider_image_path)

    def __str__(self):
        return self.image.name


class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE) 
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')
    created_at = models.DateTimeField(auto_now_add=True)
    text = models.TextField()

