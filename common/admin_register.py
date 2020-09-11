# encoding: utf-8
"""
@version: ??
@author: chenyitao
@license: Apache Licence 
@software: PyCharm
@file: admin_register.py
@time: 2019-08-06 15:27
"""
from django.contrib import admin


def easy_register(*models):
    for model_class in models:
        fields = [field.name for field in model_class._meta.fields]
        admin_class = type(model_class.__name__ + 'Admin', (admin.ModelAdmin,), {
            'list_display': fields,
            'search_fields': fields,
        })
        admin.site.register(model_class, admin_class)
