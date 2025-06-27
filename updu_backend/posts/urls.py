from django.urls import path
from .views import PostListCreateView, VotePostView, CommentCreateView

urlpatterns = [
    path('', PostListCreateView.as_view(), name='post-list-create'),
    path('<int:pk>/vote/', VotePostView.as_view(), name='vote-post'),
    path('comment/', CommentCreateView.as_view(), name='comment-post'),
]
