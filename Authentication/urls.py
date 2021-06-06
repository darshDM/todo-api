from django.urls import path
from .views import RegisterView, MyObtainTokenPairView
urlpatterns = [
    path('register',RegisterView.as_view()),
    path('login',MyObtainTokenPairView.as_view()),
]
