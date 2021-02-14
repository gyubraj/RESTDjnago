from .models import Article
from .serializers import ArticleSerializer

# import for viewsets.generics
from rest_framework import viewsets

# import for generics with mixin
from rest_framework import generics
from rest_framework import mixins

# import for Authentication
from rest_framework.authentication import SessionAuthentication,BasicAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser


# import for class base views
from rest_framework.views import  APIView

# imports while using rest_framework api_view decorators
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# imports while using functional based views
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt



# Create your views here.


# Using Model Viewsets

class ArticleList(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()

# Using Generic ViewSets

# class ArticleList(viewsets.GenericViewSet,
#                   mixins.ListModelMixin,
#                   mixins.CreateModelMixin,
#                   mixins.RetrieveModelMixin,
#                   mixins.UpdateModelMixin,
#                   mixins.DestroyModelMixin):
#     serializer_class = ArticleSerializer
#     queryset = Article.objects.all()
#     authentication_classes = [SessionAuthentication,BasicAuthentication]
#     permission_classes = [IsAuthenticated]



# generic class based views

# class ArticleList(generics.ListCreateAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
#
# class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer


# Using generics with mixins

# class GenericAPIView(generics.GenericAPIView,mixins.ListModelMixin,
#                      mixins.CreateModelMixin,mixins.UpdateModelMixin,
#                      mixins.RetrieveModelMixin,mixins.DestroyModelMixin):
#
#     serializer_class = ArticleSerializer
#     queryset = Article.objects.all()
#     # authentication_classes = [SessionAuthentication,BasicAuthentication]
#     authentication_classes = [TokenAuthentication]
#     permission_classes = [IsAuthenticated]
#     def get(self,request):
#         return self.list(request)
#
#     def post(self, request):
#         return self.create(request)
#
# class GenericArticleDetail(generics.GenericAPIView,mixins.DestroyModelMixin,
#                            mixins.UpdateModelMixin,mixins.RetrieveModelMixin):
#     serializer_class = ArticleSerializer
#     queryset = Article.objects.all()
#
#     def retrieve(self, request,pk):
#         return self.retrieve(request,pk)
#
#     def put(self,request,pk):
#         return self.update(request,pk)
#
#     def delete(self,request,pk):
#         return self.destroy(request,pk)





# Using class Based view
# class ArticleAPIView(APIView):
#
#     def get(self,request):
#         articles=Article.objects.all()
#         serializer=ArticleSerializer(articles,many=True)
#         return Response(serializer.data)
#
#     def post(self,request):
#         serializer=ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#
#
# class ArticleDetailView(APIView):
#
#     def get_object(self,id):
#         try:
#             return Article.objects.get(id=id)
#         except Article.DoesNotExist:
#             return HttpResponse(status=status.HTTP_404_NOT_FOUND)
#
#     def get(self,request,id):
#         article=self.get_object(id=id)
#         serializer=ArticleSerializer(article)
#         return Response(serializer.data)
#
#     def put(self,request,id):
#         article=self.get_object(id=id)
#         serializer=ArticleSerializer(article,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self,request,id):
#         article=self.get_object(id=id)
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)





# this uses the rest_framework api_view decorator

# @api_view(['GET','POST'])
# def article_list(request):
#     if request.method == 'GET':
#         articles=Article.objects.all()
#         serializer=ArticleSerializer(articles,many=True)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         serializer=ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#
# @api_view(['GET','PUT','DELETE'])
# def article_detail(request,id):
#     try:
#         article=Article.objects.get(id=id)
#     except:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer=ArticleSerializer(article)
#         return Response(serializer.data)
#
#     elif request.method == 'PUT':
#         serializer=ArticleSerializer(article,data=request.data)
#
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)



# these code is for functional based but not good approach
# @csrf_exempt
# def article_list(request):
#
#     if request.method == 'GET':
#         articles=Article.objects.all()
#         serializer=ArticleSerializer(articles,many=True)
#         return JsonResponse(serializer.data,safe=False)
#
#     elif request.method=='POST':
#         data=JSONParser().parse(request)
#         serializer=ArticleSerializer(data=data)
#
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data,status=201)
#         return JsonResponse(serializer.errors,status=400)
#
#
# @csrf_exempt
# def article_detail(request,pk):
#     try:
#         article=Article.objects.get(pk=pk)
#     except Article.DoesNOTExist:
#         return HttpResponse(status=404)
#     if request.method == 'GET':
#         serializer=ArticleSerializer(article)
#         return JsonResponse(serializer.data,safe=False)
#
#     elif request.method == 'PUT':
#         data=JSONParser().parse(request)
#         serializer=ArticleSerializer(article,data=data)
#
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors,status=400)
#
#     elif request.method == 'DELETE':
#         article.delete()
#         return HttpResponse(status=204)



