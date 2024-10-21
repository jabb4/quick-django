from rest_framework.response import Response
from rest_framework.decorators import api_view

from core.models import ExampleModel, APIKey, User
from .serializers import ExampleSerializer

## This works like normal Django views, inside tha @api_view you specify the method you want to use, eg. GET, POST, PUT, DELETE

@api_view(["GET"])
def example_get(request):
    data = ExampleModel.objects.all()
    serializer = ExampleSerializer(data, many=True)
    return Response(serializer.data)

@api_view(["POST"])
def example_post(request):
    ## Authorization:
    authenicated = False
    user = None
    api_key = request.headers.get("Authorization")
    if api_key:
        for key in APIKey.objects.all():
            if key.api_key == api_key:
                user = key.user
                authenicated = True
    
    if not authenicated:
        return Response({"error": "API Key invalid"}, status=401)
    else:
        return Response({"Sucess": f"API Key valid, autheticated as {user.username}"}, status=200)


        
    serializer = ExampleSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)