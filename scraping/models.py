from django.db import models

from scraping.utils import from_cyrillic_to_eng


class City(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Город')
    slug = models.CharField(max_length=50, unique=True, blank=True)

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = from_cyrillic_to_eng(self.name)
        super().save(*args, **kwargs)


class ProgrammingLanguage(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Язык программирования')
    slug = models.CharField(max_length=50, unique=True, blank=True)

    class Meta:
        verbose_name = 'Язык программирования'
        verbose_name_plural = 'Языки программирования'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = from_cyrillic_to_eng(self.name)
        super().save(*args, **kwargs)


class Vacancy(models.Model):
    vacancy_url = models.URLField(unique=True, verbose_name='Ссылка на вакансию')
    title = models.CharField(max_length=250, verbose_name='Заголовок')
    company = models.CharField(max_length=250, verbose_name='Работодатель')
    description = models.TextField(verbose_name='Описание')
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name='Город')
    programming_language = models.ForeignKey(ProgrammingLanguage, on_delete=models.CASCADE,
                                             verbose_name='Язык программирования')
    time_add = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'

    def __str__(self):
        return self.title
