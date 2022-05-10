from django.urls import path
from .views import recent_records_view, vehicles_view

urlpatterns = [
    path('recent-records', recent_records_view.as_view()),
    path('vehicles', vehicles_view.as_view())
]
