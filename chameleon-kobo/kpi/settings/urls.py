from django.urls import include, path
from kobo.urls import *

urlpatterns += [
    path(r'api/v2/utils/', include("kobo.apps.chameleon.utils.urls")),
]
