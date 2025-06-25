from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Maqola
from .serializers import Maqola_Serializer

# Create your views here.
class MaqolaListCreateAPIView(APIView):
    def get(self, request):
        maqolalar = Maqola.objects.all().order_by('number')
        serializer = Maqola_Serializer(maqolalar, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = Maqola_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


