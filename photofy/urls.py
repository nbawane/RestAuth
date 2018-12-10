from rest_auth.views import LoginView
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'group', views.GroupViewSet)
router.register(r'photos', views.PhotosViewSet)
router.register(r'groups', views.GroupDetailsViewSet)

urlpatterns = [
    # path('V1/load/',views.builddb),
    path('V1/', include(router.urls)),
    path('V1/login/', LoginView.as_view()),
    path('V1/logout/', views.Logout.as_view()),
    path('V1/download/',views.downloadmedia.as_view()),]
