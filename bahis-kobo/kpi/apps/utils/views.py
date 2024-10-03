from django.contrib.auth.models import Group
from rest_framework.exceptions import NotFound
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from .serializers import GroupSerializer, UserSerializer


class GroupList(ListAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated]


class GroupUsersListView(ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        group_name = self.kwargs.get('group_name')
        try:
            # Fetch the group by name or raise a NotFound exception if it doesn't exist
            group = Group.objects.get(name=group_name)
        except Group.DoesNotExist:
            raise NotFound(f"Group '{group_name}' not found")

        # Return all users in the group
        return group.user_set.all()
