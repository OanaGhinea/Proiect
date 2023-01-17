from django.urls import path
from .views import UtilizatoriInregistrareView

urlpatterns = [
    path('register/', UtilizatoriInregistrareView.as_view(), name='register'),

]
