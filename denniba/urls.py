from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import PlaceViewSet, VocalViewSet, PostViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'lieux', PlaceViewSet, basename='lieux')
router.register(r'vocals', VocalViewSet, basename='vocals')
router.register(r'posts', PostViewSet, basename='posts')
router.register(r'comments', CommentViewSet, basename='comments')

urlpatterns = [
    path('', include(router.urls)),
]
