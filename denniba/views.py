from rest_framework import viewsets, filters, status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response

from .models import Place, Post, Vocal, Comment
from .serializers import PlaceSerializer, PostSerializer, VocalSerializer, CommentSerializer

class PlaceViewSet(viewsets.ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['place_type']
    search_fields = ['name', 'address', 'specialties', 'contact_person']
    ordering_fields = ['created_at', 'name']

    def perform_create(self, serializer):
        user = self.request.user if self.request and self.request.user and self.request.user.is_authenticated else None
        serializer.save(created_by=user)


class VocalViewSet(viewsets.ModelViewSet):
    queryset = Vocal.objects.all()
    serializer_class = VocalSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    parser_classes = [MultiPartParser, FormParser]

    def perform_create(self, serializer):
        user = self.request.user if self.request.user.is_authenticated else None
        serializer.save(uploaded_by=user)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.select_related('author', 'audio', 'place').prefetch_related('comments')
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['content']

    def perform_create(self, serializer):
        user = self.request.user if self.request.user.is_authenticated else None
        serializer.save(author=user)

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticatedOrReadOnly])
    def comment(self, request, pk=None):
        post = self.get_object()
        data = request.data.copy()
        data['post'] = str(post.id)
        serializer = CommentSerializer(data=data)
        if serializer.is_valid():
            serializer.save(author=request.user, post=post)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
