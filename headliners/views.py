from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import *
from .serializers import *
from millennial_investor_backend import webscraper

#headliners
@api_view(['GET', 'POST'])
def headliners_list(request):
    if request.method == 'GET':
        data = Headliner.objects.all()

        headliners = []
        for headliner_model in data:
            headliner = {
                'keyword': headliner_model.keyword,
                'values':  webscraper.get_headliners(headliner_model.keyword)
            }
            headliners.append(headliner)

        return Response(headliners)

    elif request.method == 'POST':
        serializer = HeadlinerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # Delete oldest object if size is greater than
            ids = Headliner.objects.order_by("-pk").values_list("pk", flat=True)[:10]
            Headliner.objects.exclude(pk__in=list(ids)).delete()

            data = Headliner.objects.all()

            headliners = []
            for headliner_model in data:
                headliner = {
                    'keyword': headliner_model.keyword,
                    'values':  webscraper.get_headliners(headliner_model.keyword)
                }
                headliners.append(headliner)

            return Response(headliners)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'DELETE'])
def headliners_detail(request, pk):
    try:
        headliner = Headliner.objects.get(pk=pk)
    except headliner.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = HeadlinerSerializer(headliner, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        headliner.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)