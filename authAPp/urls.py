from django.urls import path
from .views import LoginAPIView, RegistrationAPIView,TestTokenValidityAPIView,RefreshTokenAPIView,LogoutAPIView

urlpatterns = [
    path('login/', LoginAPIView.as_view(), name='api-login'),
    path('register/', RegistrationAPIView.as_view(), name='api-register'),
    path('test-token/', TestTokenValidityAPIView.as_view(), name='api-test-token'),
    path('refresh-token/', RefreshTokenAPIView.as_view(), name='api-refresh-token'),
    path('logout/',LogoutAPIView.as_view(),name='logout api view')

]
