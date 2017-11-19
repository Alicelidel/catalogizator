from django.db import models
from django.utils import timezone
# Create your models here.


class Arendator(models.Model):
    AUTO_MARK = (
        ('N', 'Nissan'),
        ('M', 'Mitsubisi'),
        ('L', 'Lada'),
    )

    person = models.CharField(blank=True,max_length=30, verbose_name='ФИО')
    gos_num = models.CharField(blank=True,max_length=9, verbose_name='Гос. номер')
    box_num = models.CharField(blank=True,max_length=3, unique=True, verbose_name='Номер бокса')
    auto = models.CharField(blank=True,max_length=1, choices=AUTO_MARK, verbose_name='Марка машины')
    has_pass = models.BooleanField(default=False, verbose_name='Пропуск получен')
    registered = models.DateField(blank=True,default=timezone.now, verbose_name='Дата начала аренды')
    ended = models.DateField(blank=True, null=True, verbose_name='Дата окончания аренды')


    def get_pass(self):
        if self.has_pass == False:
            self.has_pass = True
        self.save()


    def return_pass(self):
        if self.has_pass == True:
            self.has_pass = False
        self.save()


    def __str__(self):
        return self.person



