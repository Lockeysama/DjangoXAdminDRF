import xadmin

from apps.test_app.models import Friend


class FriendAdmin(object):
    list_display = [
        'fid',
        'name',
        'gender',
        'age',
        'created_at',
        'updated_at',
    ]

    search_fields = [
        'fid',
        'name',
        'gender',
        'age',
        'created_at',
        'updated_at',
    ]

    list_filter = [
        'fid',
        'name',
        'gender',
        'age',
        'created_at',
        'updated_at',
    ]

    show_detail_fields = ['fid']

    list_editable = ['gender', 'age']


xadmin.site.register(Friend, FriendAdmin)
