from django.urls import path
from .views import TheView
urlpatterns  = [
    path('', TheView.as_view(), name='the_view')
]