from rest_framework import serializers

from rest.models import Book, Author


# class BookSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField()
#     description = serializers.CharField()
#     year = serializers.IntegerField()
#     author_id = serializers.IntegerField()
#
#     def create(self, validated_data):
#         return Book.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.description = validated_data.get('description', instance.description)
    #     instance.year = validated_data.get('year', instance.year)
    #     instance.author_id = validated_data.get('author_id', instance.author_id)
    #
    #     instance.save()
    #     return instance


class AuthorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class BookListSerializer(serializers.ModelSerializer):
    author_name = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = ('id', 'name', 'year', 'author_name')
        read_only_fields = ('author_name', )

    def get_author_name(self, obj):
        return obj.author.full_name


class BookCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('id', 'name', 'year', 'description', 'author')


class BookUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('id', 'name', 'year', 'description', 'author')


class BookRetrieveSerializer(serializers.ModelSerializer):
    author = AuthorsSerializer()

    class Meta:
        model = Book
        fields = ('id', 'name', 'year', 'description', 'author')
        extra_kwargs = {
            'author': {'write_only': True},
        }


class BookRecentBooksSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('id', 'name')




