from rest_framework import serializers
from .models import Book, Image, Author, CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id','username','name']


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'
        
        
class BookSerializer(serializers.ModelSerializer):
    image = ImageSerializer()
    author = AuthorSerializer()
    class Meta:
        model = Book
        fields = '__all__'
        