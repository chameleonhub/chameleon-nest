from django.contrib.auth.models import Group
from django.db.models import Q
from rest_framework.exceptions import NotFound
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from kpi.constants import ASSET_TYPE_SURVEY, PERM_VIEW_ASSET
from kpi.models import Asset
from kpi.utils.object_permission import get_objects_for_user

from .serializers import GroupSerializer, NexusFormSerializer, UserSerializer


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


class NexusFormListView(ListAPIView):
    serializer_class = NexusFormSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = None

    def get_queryset(self):
        user = self.request.user
        permitted_assets = get_objects_for_user(
            user,
            PERM_VIEW_ASSET,
            klass=Asset.objects.filter(asset_type=ASSET_TYPE_SURVEY),
            all_perms_required=False,
        )
        return (
            Asset.objects.filter(
                Q(owner=user) | Q(pk__in=permitted_assets.values('pk')),
                asset_type=ASSET_TYPE_SURVEY,
                date_deployed__isnull=False,
                pending_delete=False,
            )
            .only('uid', 'name', 'settings', 'date_deployed')
            .order_by('name', 'uid')
            .distinct()
        )

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response({
            'count': len(serializer.data),
            'results': serializer.data,
        })
