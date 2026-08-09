from django.urls import path
from .views import GroupList, GroupUsersListView, NexusFormListView

urlpatterns = [
    path("groups/", GroupList.as_view(), name="groups"),
    path('groups/<str:group_name>/users/', GroupUsersListView.as_view(), name='group-users-list'),
    path('nexus/forms/', NexusFormListView.as_view(), name='nexus-form-list'),
]
