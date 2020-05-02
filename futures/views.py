from rest_framework.response import Response
from rest_framework.decorators import api_view
from millennial_investor_backend import webscraper

@api_view(['GET'])
def futures_list(request):
    if request.method == 'GET':
        return Response(webscraper.get_futures())
