from django.http import HttpResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from .models import Image, Author, Book
from rest_framework.permissions import IsAuthenticated
from .serializers import (
    ImageSerializer,
    AuthorSerializer,
    BookSerializer,
    UserSerializer,
)


@api_view(["GET", "POST"])
@permission_classes((IsAuthenticated,))
def images(request):
    if request.method == "GET":
        images = Image.objects.all()
        response = ImageSerializer(images, many=True)
        return Response(response.data, status=200)
    elif request.method == "POST":
        obj = ImageSerializer(data=request.data)
        if obj.is_valid():
            obj.save()
            return Response(obj.data, status=200)
        else:
            return Response(obj.errors, status=400)


@api_view(["GET", "POST"])
@permission_classes((IsAuthenticated,))
def authors(request):
    if request.method == "GET":
        authors = Author.objects.all()
        response = AuthorSerializer(images, many=True)
        return Response(response.data, status=200)
    elif request.method == "POST":
        obj = AuthorSerializer(data=request.data)
        if obj.is_valid():
            obj.save()
            return Response(obj.data, status=200)
        else:
            return Response(obj.errors, status=400)


@api_view(["GET", "POST"])
@permission_classes((IsAuthenticated,))
def books(request):
    if request.method == "GET":
        books = Book.objects.all()
        response = BookSerializer(books, many=True)
        return Response(response.data, status=200)
    elif request.method == "POST":
        data = request.data
        obj = BookSerializer(data=request.data)
        if obj.is_valid():
            obj.save()
            return Response(obj.data, status=200)
        else:
            return Response(obj.errors, status=400)


@api_view(
    ["GET",]
)
@permission_classes((IsAuthenticated,))
def author_books(request, author_id):
    books = Book.objects.filter(author_id=author_id)
    response = BookSerializer(books, many=True)
    return Response(response.data, status=200)


@api_view(
    ["POST",]
)
def register(request):
    password = request.data["password"]
    register_serialized = UserSerializer(data=request.data)
    if register_serialized.is_valid():
        user_instance = register_serialized.save()
        user_instance.set_password(password)
        user_instance.save()
        return Response(register_serialized.data, status=201)
    else:
        return Response(register_serialized.errors, status=400)


class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)
        return Response({"access": token.key,})
