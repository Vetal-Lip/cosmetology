from django.db import models

# Create your models here.


class Category(models.Model):
    name_service = models.CharField('Название услуги', max_length=50)
    about_service = models.CharField('Описание услуги', max_length=50)

    def __str__(self):
        return self.name_service

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'


class Records(models.Model):

    category_names = Category.objects.all()
    list_category = []
    for name in category_names:
        if name.name_service:
            test = []
            test.append(name.name_service)
            test.append(name.name_service)
            tuple_category = tuple(test)
            print(tuple_category)
            list_category.append(tuple_category)
    CHOICES_CATEGORY = tuple(list_category)

    name = models.CharField('Имя', max_length=100)
    email = models.EmailField('Электронный адрес ', max_length=100)
    procedure = models.CharField(
        'Процедура', max_length=100, choices=CHOICES_CATEGORY)
    date = models.DateField('Дата записи')
    time = models.TimeField('Время записи')
    newsletter = models.BooleanField(
        'Хочу получать рассылку новостей', default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Запись на процедуру'
        verbose_name_plural = 'Записи на процедуры'
