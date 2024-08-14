from django.db import models

# Create your models here.

class Posts(models.Model):
    title = models.CharField('Заголовок', max_length=100)
    anouncement = models.CharField('Анонс', max_length=255)
    text = models.TextField('Текст')
    date = models.DateField('Дата')

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


# class Posts(models.class (models.Model):

#     class Meta:
#         verbose_name = _("")
#         verbose_name_plural = _("s")

#     def __str__(self):
#         return self.name

#     def get_absolute_url(self):
#         return reverse("_detail", kwargs={"pk": self.pk})
