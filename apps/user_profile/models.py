from django.urls import reverse

from django.contrib.auth.models import AbstractUser
from django.db import models


class UserModel(AbstractUser):

    first_name = models.CharField(verbose_name="Имя", max_length=30, blank=True)
    middle_name = models.CharField(verbose_name='Отчество', max_length=30, blank=True)
    last_name = models.CharField(verbose_name='Фамилия', max_length=30, blank=True)
    date_birth = models.DateField(verbose_name='День рождения', blank=True, null=True)
    slug = models.SlugField(default=None, blank=True, null=True)

    def __str__(self):
        return self.username

    def get_full_name(self):
        return ' '.join([self.last_name, self.first_name, self.middle_name])

    def get_absolute_url(self):
        return reverse('user_profile:view_profile', args=[self.id])
