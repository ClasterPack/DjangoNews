from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
    path('', views.news_view, name='home'),
    path('news/create', views.post_create_view, name='create'),
    path('news/<slug:slug>/', views.post_details, name='post_detail')
] + static(settings.MEDIA_URL,
           document_root=settings.MEDIA_ROOT)
