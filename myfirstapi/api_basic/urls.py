
from django.urls import path,include

# all for viewSets
from rest_framework.routers import DefaultRouter
from .views import ArticleList
router=DefaultRouter()
router.register('articleapi',ArticleList,basename='article')

# from .views import ArticleDetail,ArticleList

# from .views import GenericAPIView,GenericArticleDetail

# from .views import ArticleAPIView,ArticleDetailView

# from .views import article_list,article_detail

urlpatterns= [
    # path('articleapi/',article_list),
    # path('articleapi/<int:id>/',article_detail),
    # path('articleapi/',ArticleAPIView.as_view()),
    # path('articleapi/<int:id>/',ArticleDetailView.as_view()),
    # path('articleapi/',GenericAPIView.as_view()),
    # path('articleapi/<int:pk>/',GenericArticleDetail.as_view()),
    # path('articleapi/',ArticleList.as_view()),
    # path('articleapi/<int:pk>/',ArticleDetail.as_view(),)
    path('',include(router.urls)),


]