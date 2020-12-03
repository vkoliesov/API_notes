from rest_framework import serializers
from notes.models import Note
from accounts.models import UserProfile

from django.contrib.auth import get_user_model

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        queryset = model.objects.all()
        fields = ('id', 'username', 'email', 'password', 'first_name', 'last_name', 'is_superuser')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = UserProfile.Meta.model(**validated_data)
        user.save()
        return user

    def update(self, instance, validated_data):
        instance.set_password(validated_data.pop('password', ''))
        return super().update(instance, validated_data)


class NoteSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField(read_only = True)

    def get_author(self, obj):
        return obj.author.username
    class Meta:
        model = Note
        fields = '__all__'


class ThinNoteSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='notes-detail')
    class Meta:
        model = Note
        fields = ('id', 'title', 'url')


# class NoteSerializer(serializers.Serializer):

#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(required=True, max_length=50)
#     text = serializers.CharField(required=False, allow_blank=True)

#     def create(self, validated_data):
#         return Note.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.text = validated_data.get('text', instance.text)
#         instance.save()
#         return instance