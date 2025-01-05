from rest_framework.serializers import ModelSerializer
from library.models import Books, Author

class BooksSerializer(ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'

class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'