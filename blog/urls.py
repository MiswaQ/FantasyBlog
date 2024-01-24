from .views import PostList, PostDetail, PostLike, delete, EditComments
from django.urls import path


urlpatterns = [
    path('', PostList.as_view(),  name='home'),
    path('<slug:slug>/', PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', PostLike.as_view(), name='post_like'),
    path('delete/<int:id>', delete, name='delete'),
    path('edit/<int:pk>', EditComments.as_view(), name='edit_comment'),
]
