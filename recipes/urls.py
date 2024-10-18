from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RecipeViewSet, ImageViewSet, TagViewSet, RecipeTagViewSet

router = DefaultRouter()
router.register(r'recipes', RecipeViewSet)
router.register(r'images', ImageViewSet)
router.register(r'tags', TagViewSet)
router.register(r'recipe-tags', RecipeTagViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
