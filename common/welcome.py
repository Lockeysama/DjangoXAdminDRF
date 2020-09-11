# encoding: utf-8
"""
@version: ??
@author: chenyitao
@license: Apache Licence 
@software: PyCharm
@file: welcome.py
@time: 2019-08-07 17:37
"""
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.authentication import SessionAuthentication, BasicAuthentication


@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def welcome(request):
    """
    The api root for affective cloud server. This can be used for server validity check. Moreover it will
    return some useful URLs. It can be accessed from browser directly.

    ## Authentication

    Affective cloud server needs authentication always. Three kinds of authentication exist.

    1. **JWT Token:** For staff use only, users are managed under django admin.

    ## Versioning

    Affective cloud API adopt accept header versioning. which means a request version can be added to
    HTTP header. If not specified, the server will use the default version, currently only `v1`
    version is available.

    `Accept: application/json; version=v1`
    """
    root_url = reverse(welcome, request=request)
    return Response(
        {'API docs': root_url + 'docs/', 'Admin portal': root_url + 'xadmin/'}
    )
