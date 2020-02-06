
from django.urls import path
from inetapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   # path('', views.home),
   path('', views.show, name='home'),
   path('submitted/', views.sav, name='saav'),
   path('hello/', views.retrieve, name='hello'),
   path('edit/<int:id>/', views.edit, name='edits'),
   path('delete/<int:id>/', views.delete, name='del'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


