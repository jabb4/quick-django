from rest_framework.response import Response
from rest_framework.decorators import api_view

from core.models import ExampleModel
from .serializers import ExampleSerializer

## This works like normal Django views, inside tha @api_view you specify the method you want to use, eg. GET, POST, PUT, DELETE

@api_view(["GET"])
def example_get(request):
    data = ExampleModel.objects.all()
    serializer = ExampleSerializer(data, many=True)
    return Response(serializer.data)

@api_view(["POST"])
def example_post(request):
    serializer = ExampleSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)