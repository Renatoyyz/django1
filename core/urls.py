from django.urls import path
from django.contrib.auth import views as auth_views

from .views import index, contato, produto

urlpatterns = [
    path("", index, name='index'),
    path("contato", contato, name='contato'),
    path('produto/<int:pk>', produto, name='produto'),
]