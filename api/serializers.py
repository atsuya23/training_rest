from rest_framework import serializers
from .models import Training, Content, TrainingType
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
    class Meta:
        model = Training
        fields = ('id', 'review', 'evaluation', 'place', 'created_at', 'updated_at')


class ContentSerializer(serializers.ModelSerializer):
    id_training = TrainingSerializer()

    class Meta:
        model = Content
        fields = '__all__'


class TrainingTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainingType
        fields = '__all__'


