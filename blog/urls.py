from django.urls import path
from .views import HomeView, ArticleDetailView, AddPostView, UpdatePostView, DeletePostView, AddCommentView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='detail'),
    path('add_post/', AddPostView.as_view(), name='add'),
    path('article/update/<int:pk>', UpdatePostView.as_view(), name='update'),
    path('article/delete/<int:pk>', DeletePostView.as_view(), name='delete'),
    path('article/<int:pk>/comment/',
         AddCommentView.as_view(), name='add_comment'),


]
