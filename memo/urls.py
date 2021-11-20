from django.urls import path
from django.conf.urls import include
from rest_framework import routers

from memo.views import MemoViewSet

router = routers.DefaultRouter()
router.register('memo', MemoViewSet, basename='memo')

urlpatterns = [
    path('', include(router.urls)),
]
