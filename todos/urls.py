from django.urls import path

from .views import home , todoview

urlpatterns = [
    path('' , todoview , name="todo"),
]