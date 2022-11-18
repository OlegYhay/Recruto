from django.urls import path
from .views import HelloWorld

urlpatterns = [
    path('welcome/', HelloWorld.as_view(), name='welcome'),
]
