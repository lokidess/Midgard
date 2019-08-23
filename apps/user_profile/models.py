from django.contrib.auth.models import AbstractUser
from django.db import models


class UserModel(AbstractUser):

    first_name = models.CharField(verbose_name="Ім'я", max_length=30, blank=True)
    middle_name = models.CharField(verbose_name='По батькові', max_length=30, blank=True)
    last_name = models.CharField(verbose_name='Прізвище', max_length=30, blank=True)
    date_birth = models.DateField(verbose_name='День рождения', blank=True, null=True)

    def __str__(self):
        return self.username
