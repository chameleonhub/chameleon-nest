from django.urls import include, path
from kobo.urls import *

urlpatterns += [
    # path(r'desk/', include("kobo.apps.desk.urls")),
    path(r'api/v2/utils/', include("kobo.apps.bahis.utils.urls")),
]
