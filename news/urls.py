from rest_framework.routers import SimpleRouter
from .views import PostViewSet, CommentView, CommentDetailView
from django.urls import path, include

router = SimpleRouter()
router.register(r'posts', PostViewSet)

urlpatterns = [
    path('posts/<int:post_id>/comments/', CommentView.as_view()),
    path(
        'posts/<int:post_id>/comments/<int:pk>/',
        CommentDetailView.as_view()
    ),
    path('comments/<int:pk>/', CommentDetailView.as_view()),
    path('', include(router.urls))
]
