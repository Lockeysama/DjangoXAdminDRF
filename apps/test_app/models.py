from django.db import models

# Create your models here.
from common.model_mixins import CreatedUpdatedMixin


class Friend(CreatedUpdatedMixin):

    GENDER = ((0, '女'), (1, '男'), (2, '保密'))

    fid = models.AutoField(primary_key=True, verbose_name='ID', help_text='Friend ID')

    name = models.CharField(
        max_length=16, null=False, verbose_name='姓名', help_text='姓名'
    )

    gender = models.SmallIntegerField(
        choices=GENDER, blank=True, verbose_name='性别', help_text='性别'
    )

    age = models.IntegerField(null=True, blank=True, verbose_name='年龄', help_text='年龄')

    class Meta:
        verbose_name = '朋友'

        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
