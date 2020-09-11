"""
1 Xadmin介绍
直接替换掉Django自带的admin系统，并提供了很多有用的东西；完全的可扩展的插件支持，基于Twitter Bootstrap的漂亮UI。

2 Xadmin特点
完全替代Django admin
支持基于Twitter Bootstrap的UI主题
支持可扩展的插件
更好的过滤器，日期范围，数量范围等
内置xls，csv，xml和json格式数据导出
仪表板页面和小部件支持 （暂时用不到）
现场书签
完整的CURD方法（增删改查）

3. Github
# 较久未更新
https://github.com/sshwsfc/xadmin

4. 资料
https://sshwsfc.github.io/xadmin/
https://www.jianshu.com/p/49eb568c9a25
https://blog.csdn.net/bocai_xiaodaidai/article/details/94395604


"""

from django.contrib.auth import get_user_model

import xadmin

from apps.users.models import Account
from xadmin.plugins.auth import UserAdmin


class GlobalSetting(object):

    site_title = 'DjangoXAdminDRF'

    site_footer = 'DjangoXAdminDRF'

    menu_style = 'accordion'


xadmin.site.register(xadmin.views.CommAdminView, GlobalSetting)


class BaseSettings(object):
    enable_themes = True  # 使用主题功能
    use_bootswatch = True


xadmin.site.register(xadmin.views.BaseAdminView, BaseSettings)


class AccountAdmin(UserAdmin):
    list_display = [
        'id',
        'username',
        'mobile',
        'email',
        'first_name',
        'last_name',
        'is_staff',
        'is_active',
        'date_joined',
    ]

    search_fields = [
        'id',
        'username',
        'mobile',
        'email',
        'first_name',
        'last_name',
        'is_staff',
        'is_active',
        'date_joined',
    ]

    list_filter = [
        'id',
        'username',
        'mobile',
        'email',
        'first_name',
        'last_name',
        'is_staff',
        'is_active',
        'date_joined',
    ]


xadmin.site.unregister(get_user_model())
xadmin.site.register(Account, AccountAdmin)
