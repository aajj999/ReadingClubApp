from django.urls import include, path
from rest_framework import routers
from ReadingClub.RCApp.views import BookViewSet, AuthorViewSet, UserViewSet, GroupViewSet, TypeViewSet

router = routers.DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'authors', AuthorViewSet)
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'type', TypeViewSet)

urlpatterns = [
   path('', include(router.urls)),
]