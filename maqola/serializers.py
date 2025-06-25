from rest_framework import serializers
from .models import Maqola


class Maqola_Serializer(serializers.ModelSerializer):
    journal_information = serializers.ReadOnlyField()

    class Meta():
        model = Maqola
        fields = ['id', 'number', 'title', 'format', 'publication_type', 'journal_name', 'volume', 'issue', 'published_date', 'pages', 'bet_soni', 'mualliflar_soni', 'authors', 'journal_information',]