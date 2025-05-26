from django.urls import path
from .views import RegisterView, UpdateUserView, LogoutView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('update/', UpdateUserView.as_view(), name='update_user'),
    path('logout/', LogoutView.as_view(), name='logout'),
]