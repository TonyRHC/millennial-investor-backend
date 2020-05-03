from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import *
from .serializers import *
from millennial_investor_backend import webscraper

#Stocks
@api_view(['GET', 'POST'])
def stocks_list(request):
    if request.method == 'GET':
        return Response(get_all_stocks(), status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = StockSerializer(data=request.data)

        if serializer.is_valid() and webscraper.get_stock(request.data['ticker']) != None:
            serializer.save()
            return Response(get_all_stocks(), status=status.HTTP_201_CREATED)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'DELETE'])
def stocks_detail(request, pk):
    try:
        stock = Stock.objects.get(pk=pk)
    except Stock.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = StockSerializer(stock, data=request.data,context={'request': request})
        if serializer.is_valid() and webscraper.get_stock(request.data['ticker']) != None:
            serializer.save()
            return Response(get_all_stocks(), status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        stock.delete()
        return Response(get_all_stocks(), status=status.HTTP_200_OK)

def get_all_stocks():
    data = Stock.objects.all()
    stocks = []
    for stock_model in data:
        stock = {
            'pk': stock_model.pk,
            'data': webscraper.get_stock(stock_model.ticker)
        }
        stocks.append(stock)
    return stocks