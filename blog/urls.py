from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^category/$', views.CategoryListAPIView.as_view()),
    url(r'^category/(?P<pk>[\d-]+)$', views.CategoryDetailsAPIView.as_view()),

    url(r'^tag/$', views.TagListAPIView.as_view()),
    url(r'^tag/(?P<pk>[\d-]+)$', views.TagDetailsAPIView.as_view()),

    url(r'^article/$', views.ArticleListAPIView.as_view()),
    url(r'^article/(?P<pk>[\d-]+)$', views.ArticleDetailsAPIView.as_view()),

]
