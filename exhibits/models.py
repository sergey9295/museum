from django.db import models

class Exhibit(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название экспозиции")
    description = models.TextField(verbose_name="Описание экспозиции")
    floor = models.IntegerField(verbose_name="Этаж",
                                choices=[(1, 'Первый этаж'), (2, 'Второй этаж'), (3, 'Третий этаж')])
    is_open = models.BooleanField(default=True, verbose_name="Открыта для посещения")

    def __str__(self):
        return self.name


class ExhibitItem(models.Model):
    exhibit = models.ForeignKey(Exhibit, on_delete=models.CASCADE, related_name='items')
    name = models.CharField(max_length=200, verbose_name="Название экспоната")
    description = models.TextField(verbose_name="Описание экспоната")
    image = models.ImageField(upload_to='exhibit_images/', verbose_name="Фотография экспоната")
    status = models.CharField(max_length=50, choices=[
        ('available', 'Доступен'),
        ('restoration', 'На реставрации'),
        ('storage', 'В запаснике'),
        ('on_exhibition', 'На выставке')
    ], default='Доступен', verbose_name="Статус экспоната")

    def __str__(self):
        return self.name

