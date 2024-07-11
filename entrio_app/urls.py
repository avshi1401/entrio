from django.urls import path

from entrio_app import views

urlpatterns = [
    path('get_repository_details/<str:repository_first_name>/<str:repository_last_name>', views.get_repository_details),
]
