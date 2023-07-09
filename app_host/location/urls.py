from django.contrib import admin
from django.urls import path, include
from .import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about-us/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('paiement/', views.paiement, name='paiement'),
    path('news/', views.news, name='news'),
    path('read_more/', views.read_more, name='read_more'),
    path('services/', views.services, name='services'),
    path('store/', include('store.urls')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
