from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("register/",views.registerUser,name ="register-user"),
    path("getmessages/",views.getMessages,name = "get-messages"),
    path("sendmessage/",views.sendMessage,name = "send-message"),
    
]
