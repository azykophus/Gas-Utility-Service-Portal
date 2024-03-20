from django.urls import path
from django.urls import path
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from .views import signup_view, home
from . import views
from django.contrib.auth import views as auth_views
from .views import signup
from django.urls import path
from django.contrib.auth.views import LoginView


urlpatterns = [
    path('', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('signup/', signup_view, name='signup'),
    path('home/', home, name='home'),
    path('submit/', views.submit_request, name='submit_request'),
    path('track/', views.track_requests, name='track_requests'),
    path('logout/', LogoutView.as_view(next_page='/login/'), name='logout'),

]
