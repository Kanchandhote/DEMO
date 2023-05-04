from django.urls import path
from f2api import views
 
 
urlpatterns = [
    path('upload/', views.ProfileView.as_view(), name='upload'),
    path('upload_list/', views.ProfileView.as_view(), name='upload_list'),
 ]
 
#  http://127.0.0.1:8000/api/upload_list/