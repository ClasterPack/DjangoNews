from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.news_view, name='home'),
    path('news/<slug:slug>/', views.post_details, name='post_detail')
] + static(settings.MEDIA_URL,
           document_root=settings.MEDIA_ROOT)
