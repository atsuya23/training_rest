from rest_framework.permissions import AllowAny
from rest_framework import viewsets

from .models import Memo
from .serializers import MemoSerializer


class MemoViewSet(viewsets.ModelViewSet):
    queryset = Memo.objects.all()
    serializer_class = MemoSerializer
    permission_classes = (AllowAny,)
    filterset_fields = ['category', 'created_at']
