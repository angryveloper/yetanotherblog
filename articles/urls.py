from django.urls import path

from . import views


# app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('article/<int:pk>', views.article_detail, name='article_detail'),
    path('article/new/', views.new_article, name='new_article'),
    path('article/<int:pk>/edit/', views.edit_article, name='edit_article'),
    path('article/<int:pk>/comment/', views.leave_comment, name='leave_comment'),
    path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
]
