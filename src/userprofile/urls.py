from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from userprofile.views import MyTokenObtainPairView, ForgotPasswordView, ResetPasswordView

urlpatterns = [
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('forgot-password/', ForgotPasswordView.as_view(), name='forgot_password'),
    path('reset-password/', ResetPasswordView.as_view(), name='reset_password'),
]