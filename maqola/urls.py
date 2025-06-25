from django.urls import path
from .views import MaqolaListCreateAPIView, ExportMaqolaDocxView

urlpatterns = [
    path('maqolalar/', MaqolaListCreateAPIView.as_view(), name='maqola-list-create'),
    path('maqolalar/export-docx/', ExportMaqolaDocxView.as_view(), name='maqola-export'),
]
