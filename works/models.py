from django.db import models


class Works(models.Model):
    name = models.CharField(max_length=256)
    descriptions = models.CharField(max_length=256)
    photo = models.ImageField(upload_to='works_image', null=True, blank=True)

    class Meta:
        verbose_name = 'Страница с работами'
        verbose_name_plural = 'Страница с работами'

    def __str__(self):
        return f'{self.name}'
