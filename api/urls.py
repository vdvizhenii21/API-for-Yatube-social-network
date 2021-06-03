from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, FollowViewSet, GroupViewSet
from rest_framework.authtoken import views


router_v1 = DefaultRouter()
router_v1.register('posts', PostViewSet, basename='api_posts')
router_v1.register(
    r'posts/(?P<post_id>[^/.]+)/comments', CommentViewSet, basename='api_comments'
)
router_v1.register('follow', FollowViewSet, basename='api_follow')
router_v1.register('group', GroupViewSet, basename='api_group')

urlpatterns = [
    path('', include(router_v1.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
