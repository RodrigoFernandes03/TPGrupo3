from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.home),
    path("categoria/<slug:val>", views.CategoriaView.as_view(),name='categoria'),

    #login authentication
    path('registration/', views.CustomerRegistrationView.as_view(), name = 'customerregistration')

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)