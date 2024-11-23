from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('ciolk', views.ciolk, name='ciolk'),
    path('perelman', views.perelman, name='perelman'),
    path('kapica', views.kapica, name='kapica')
]
