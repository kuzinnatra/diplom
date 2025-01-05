from django.urls import path
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from users.apps import UsersConfig
from users.views import UserListApiView, UserRetrieveApiView, UserCreateApiView, UserUpdateApiView, UserDestroyApiView

app_name = UsersConfig.name


urlpatterns = [
    path('user/', UserListApiView.as_view(), name='user_list'),
    path('user/<int:pk>/', UserRetrieveApiView.as_view(), name='user_retrieve'),
    path('register/', UserCreateApiView.as_view(), name='register'),
    path('user/<int:pk>/delete/', UserDestroyApiView.as_view(), name='user_delete'),
    path('user/<int:pk>/update/', UserUpdateApiView.as_view(), name='user_update'),
    path('login/', TokenObtainPairView.as_view(permission_classes=(AllowAny,)), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(permission_classes=(AllowAny,)), name='token_refresh'),
]

