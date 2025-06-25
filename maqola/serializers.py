from rest_framework import serializers
from .models import Maqola


class Maqola_Serializer(serializers.ModelSerializer):
    journal_information = serializers.ReadOnlyField()

    class Meta():
        model = Maqola
        fields = ['talaba_fish', 'fakultet', 'fakultet_raqami', 'guruh_raqami', 'number', 'title', 'format', 'publication_type', 'journal_name', 'volume', 'issue', 'published_date', 'pages', 'bet_soni', 'mualliflar_soni', 'authors', 'journal_information',]