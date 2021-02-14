from rest_framework import serializers
from .models import Article

# This is modelSerializer which auto implement create and update method so prefer to use this one
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model=Article
        # fields define what you should give or get
        fields=['id', 'title','author','email']

        # to make all fields
        # fields='__all__'



# this will require to provide all fields of the model
# class ArticleSerializer(serializers.Serializer):
#     title=serializers.CharField(max_length=100)
#     author=serializers.CharField(max_length=100)
#     email=serializers.EmailField(max_length=100)
#     date=serializers.DateTimeField()
#
#     def create(self, validated_data):
#         return Article.objects.create(validated_data)
#
#     def update(self,instance,validated_data):
#         instance.title=validated_data.get('title',instance.title)
#         instance.author = validated_data.get('author', instance.author)
#         instance.email = validated_data.get('email', instance.email)
#         instance.date = validated_data.get('date', instance.date)
#         instance.save()
#         return instance

