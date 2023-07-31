from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from .models import MotivationQuote
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import MotivationQuoteSerializer
from rest_framework import status
import random

@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def motivation_quote_list(request):
    if request.method == 'GET':
        quotes = MotivationQuote.objects.all()
        serializer = MotivationQuoteSerializer(quotes, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        if isinstance(request.data, list):
            serializer = MotivationQuoteSerializer(data=request.data, many=True)
        else:
            serializer = MotivationQuoteSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def random_motivation_quote(request):
    quotes = MotivationQuote.objects.all()
    if quotes:
        random_quote = random.choice(quotes)
        serializer = MotivationQuoteSerializer(random_quote)
        return Response(serializer.data)
    else:
        return Response({"message": "No quotes available."}, status=404)