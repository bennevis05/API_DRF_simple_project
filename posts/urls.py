from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import UserViewSet, PostViewSet


router = SimpleRouter()
router.register('users', UserViewSet, base_name='users')
router.register('', PostViewSet, base_name='posts')

# Usage without routers
# urlpatterns = [
#     path('', PostList.as_view()),
#     path('<int:pk>/', PostDetail.as_view()),
#     path('users/', UserList.as_view()),
#     path('users/<int:pk>/', UserDetail.as_view()),
# ]

urlpatterns = router.urls
