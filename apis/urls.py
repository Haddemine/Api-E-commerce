from django.urls import path

from apis.views import DetailClient, ListClient

app_name='apis'
urlpatterns=[
    path('client',ListClient.as_view(), name='listclient'),
    path('client/<int:pk>/',DetailClient.as_view()),
]           