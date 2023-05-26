from rest_framework import serializers
from django.contrib.auth.models import User, Group
from ReadingClub.RCApp.models import Book, Author, Type

class BookSerializer(serializers.ModelSerializer):
   class Meta:
       model = Book
       fields = ['title', 'author', 'type']

class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = ['name']

class TypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Type
        fields = ['typeName']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']