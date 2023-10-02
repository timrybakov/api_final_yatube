from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import PostViewSet, CommentViewSet, GroupViewSet, FollowViewSet

v1_router = DefaultRouter()
v1_router.register(r'v1/posts', PostViewSet)
v1_router.register(r'v1/groups', GroupViewSet)
v1_router.register(
    r'v1/posts/(?P<post_id>\d+)/comments',
    CommentViewSet, basename='comments'
)
v1_router.register(r'v1/follow', FollowViewSet, basename='followers')

urlpatterns = [
    path('', include(v1_router.urls)),
    path('v1/', include('djoser.urls.jwt')),
]
