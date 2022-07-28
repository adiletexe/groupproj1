from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('find/<str:pk>', views.readmore, name='find'),
    path('add/', views.add, name='add'),
    path('all/', views.add, name='all'),
    path('electronics/', views.add, name='electronics'),
    path('jewelry/', views.add, name='jewelry'),
    path('clothes/', views.add, name='clothes'),
    path('people/', views.add, name='people'),
    path('people/', views.add, name='pets'),
    path('importantsheets/', views.add, name='importantsheets'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)