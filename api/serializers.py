from rest_framework import serializers
from .models import Training, Content, Image, TrainingType
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class TrainingSerializer(serializers.ModelSerializer):
    # created_at = serializers.DateTimeField(format="%Y/%m/%d")

    class Meta:
        model = Training
        fields = ('id', 'review', 'evaluation', 'place', 'created_at', 'updated_at')


class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ('id', 'id_training', 'training_type', 'weight', 'set1', 'set2', 'set3')


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('id', 'name', 'image')


class TrainingTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainingType
        fields = ('id', 'type')

