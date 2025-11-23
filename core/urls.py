from django.contrib.auth.decorators import login_required
from django.contrib import admin
from django.urls import path, include
from accounts import views as account_views
from django.contrib.auth import views as auth_views


urlpatterns = [
   
    path("", account_views.home, name="home"),

   
    path("signup/", account_views.signup, name="signup"),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="accounts/login.html"),
        name="login",
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(next_page="login"),
        name="logout",
    ),

 
    path("students/", include("students.urls")),

    
    path("exams/", include("exams.urls")),

   
    path("admin/", admin.site.urls),
]
