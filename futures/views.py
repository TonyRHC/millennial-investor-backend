from rest_framework.response import Response
from rest_framework.decorators import api_view
from .webscraper import get_futures

@api_view(['GET'])
def futures_list(request):
    if request.method == 'GET':
        return Response(get_futures())
