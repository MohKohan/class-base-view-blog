from django.urls import path
from blog.views import *


from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.urls import re_path
from rest_framework import permissions
from rest_framework.routers import DefaultRouter
from drf_yasg.views import get_schema_view
from drf_yasg import openapi



schema_view = get_schema_view(
   openapi.Info(
      title="blog API",
      default_version='v1',
      description="description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="mohadeseshajarikohann@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns=[
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    
    
    path('',project.as_view(),name="projects"),
    path('<slug:slug>/',projectDetail.as_view(),name="project-detail"),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    
    

]
router=DefaultRouter()
router.register(r'api/project',sightseeingPlacesViewSet)
urlpatterns += router.urls







