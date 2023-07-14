from django.urls import path
from .views import RegisterView
from .views import LoginView
from .views import UserView
from .views import LogoutView

urlpatterns = [
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),
    path('user',UserView.as_view()),
    path('logout',LogoutView.as_view())


]