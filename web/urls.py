from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt import views as auth_views


router = DefaultRouter()

urlpatterns = [
    path('api/v1/login/', auth_views.TokenObtainPairView.as_view(), name='login'),
    path('api/v1/login/refresh/', auth_views.TokenRefreshView.as_view(), name='login_refresh'),
    path('api/v1/', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)