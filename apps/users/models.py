from django.contrib.auth.models import AbstractUser
from django.db import models


class Account(AbstractUser):

    mobile = models.CharField(
        max_length=16,
        null=True,
        blank=True,
        unique=True,
        verbose_name='手机号',
        help_text='手机号',
    )

    class Meta(AbstractUser.Meta):

        verbose_name = '账户信息'

        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username
