
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from f2api import views


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/', include('f2api.urls')),
    path('profile/', views.profile.as_view()),   
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
