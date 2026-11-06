from django.contrib import admin
from django.urls import include,path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from drf_spectacular.views import SpectacularAPIView,SpectacularSwaggerView
from tasks.views import RegisterView,TaskViewSet
router=DefaultRouter(); router.register("tasks",TaskViewSet,basename="task")
urlpatterns=[path("admin/",admin.site.urls),path("api/auth/register/",RegisterView.as_view()),path("api/auth/token/",TokenObtainPairView.as_view()),path("api/auth/token/refresh/",TokenRefreshView.as_view()),path("api/",include(router.urls)),path("api/schema/",SpectacularAPIView.as_view(),name="schema"),path("api/docs/",SpectacularSwaggerView.as_view(url_name="schema"))]
