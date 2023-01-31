"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from inflearn import views as inflearn_views
from accounts import views as accounts_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),

    path("", inflearn_views.home, name="home"),

    path("courses/", inflearn_views.courses, name="courses"),
    path("open_course/", inflearn_views.open_course, name="open_course"),
    path('course_detail/<int:course_id>', inflearn_views.course_detail, name='course_detail'),
    path("open_lecture/<int:course_id>", inflearn_views.open_lecture, name="open_lecture"),
    path("course_detail/<int:course_id>/lecture_detail/<int:lecture_id>", inflearn_views.lecture_detail, name="lecture_detail"),

    path('login/', accounts_views.login, name='login'),
    path('logout/', accounts_views.logout, name='logout'),
    path('signup/', accounts_views.signup, name='signup'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)