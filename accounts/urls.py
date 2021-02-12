from django.conf.urls import url
from django.contrib.auth import views as auth_views
from accounts import views
from accounts.views import Signup
from django.urls import path


app_name = 'accounts'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'),
         name='login'),
    # path('logout/', views.logout, name="logout"),
    path('signup/', Signup.as_view(), name='signup'),
]
