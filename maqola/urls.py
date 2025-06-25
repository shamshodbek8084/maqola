from django.urls import path
from .views import MaqolaListCreateAPIView

urlpatterns = [
    path('maqolalar/', MaqolaListCreateAPIView.as_view(), name='maqola-list-create'),
]
