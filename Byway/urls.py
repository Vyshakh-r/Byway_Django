from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Index page (Categories) connected to `home`
    path('home/', views.home_view, name='home_view'),  # Home page (Courses) connected to `home_view`
    path('courses/', views.courses, name='courses'),
    path('home/courses',views.courses, name='courses')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)