from rest_framework import viewsets

from api.permissions import IsAdminOrReadOnly
from api.serializers import ProjectSerializer

from portfolio.models import Project


class ProjectViewSet(viewsets.ModelViewSet):

    serializer_class = ProjectSerializer
    permission_classes = (IsAdminOrReadOnly, )

    def get_queryset(self):
        return Project.objects.all()
