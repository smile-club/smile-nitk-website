# urls.py

from django.urls import path
from .views import PostDetailView ,team_list_view,event_list,blog_list,post_detail,event_detail,display_youtube_videos,gallery,home,image_group_images
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path('event', TemplateView.as_view(template_name='t_event.html'), name='event'),
    path('post/<uuid:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('about/', team_list_view, name='team-list'),
    path('post/<uuid:post_id>/', post_detail, name='post-detail'),
    path('timeline/', event_list, name='event-list'),
    path('blogs/', blog_list, name='blogs-list'),
    path('events/<int:event_id>/', event_detail, name='event_detail'),
    path('youtube-videos/', display_youtube_videos, name='display_youtube_videos'),
    path('gallery/', gallery, name='gallery'),
    path('', home, name='home'),
    path('gallery/<int:group_id>/', image_group_images, name='image_group_images'),
    
    # Other URL patterns as needed
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
