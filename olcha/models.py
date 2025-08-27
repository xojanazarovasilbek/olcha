from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='category/images/')
    slug = models.SlugField(unique=True)

    parent = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        related_name='children',
        null=True,
        blank=True
    )


    def __str__(self):
        if self.parent:
            return f'{self.parent.title} -> {self.title}'
        return self.title
    
    class Meta:
        verbose_name_plural = 'categories'


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='product')
    title = models.CharField(max_length=111)
    desc = models.TextField(max_length=255, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='category/images/product/')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.category}, {self.title}"