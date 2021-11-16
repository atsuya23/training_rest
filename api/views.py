from rest_framework.permissions import AllowAny
from rest_framework import generics
from rest_framework import viewsets

from .serializers import TrainingSerializer, ContentSerializer, UserSerializer, ImageSerializer, TrainingTypeSerializer
from .models import Training, Content, Image, TrainingType


class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)


class TrainingListView(generics.ListAPIView):
    queryset = Training.objects.all()
    serializer_class = TrainingSerializer
    permission_classes = (AllowAny,)


class TrainingRetrieveView(generics.RetrieveAPIView):
    queryset = Training.objects.all()
    serializer_class = TrainingSerializer
    permission_classes = (AllowAny,)


class TrainingViewSet(viewsets.ModelViewSet):
    queryset = Training.objects.all()
    serializer_class = TrainingSerializer
    permission_classes = (AllowAny,)
    filterset_fields = ['created_at', 'place', 'evaluation']


class ContentListView(generics.ListAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    permission_classes = (AllowAny,)




class ContentRetrieveView(generics.RetrieveAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    permission_classes = (AllowAny,)


class ContentViewSet(viewsets.ModelViewSet):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    permission_classes = (AllowAny,)
    filterset_fields = ['id_training', 'training_type', 'weight', 'created_at']


class ImageListView(generics.ListAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = (AllowAny,)


class ImageRetrieveView(generics.RetrieveAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = (AllowAny,)


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = (AllowAny,)


class TrainingTypeListView(generics.ListAPIView):
    queryset = TrainingType.objects.all()
    serializer_class = TrainingTypeSerializer
    permission_classes = (AllowAny,)


class TrainingTypeViewSet(viewsets.ModelViewSet):
    queryset = TrainingType.objects.all()
    serializer_class = TrainingTypeSerializer
    permission_classes = (AllowAny,)

