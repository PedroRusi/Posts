from django.db import models

# Create your models here.
class Post(models.Model):
    CATEGORY = [
        ('Животные', 'Животные'),
        ('Игры', 'Игры'),
        ('Еда', 'Еда'),
        ('Новости','Новости'),
        ('Учёба','Учёба')
    ]
    name = models.CharField(max_length=35)
    category = models.CharField(max_length=9,choices=CATEGORY)
    publicate = models.BooleanField(default=True)
    text = models.TextField()
    image_url = models.URLField()

    def __str__(self):
        return self.name