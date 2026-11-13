from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(["GET"])
def health(request):
    return Response({"service":"HARMONYMUGZ BANK","status":"development","notice":"No real banking services are connected."})

@api_view(["GET"])
def bank(request):
    return Response({"portal":"BANK","status":"placeholder"})

@api_view(["GET"])
def partner(request):
    return Response({"portal":"PARTNER","status":"placeholder"})

@api_view(["GET"])
def control(request):
    return Response({"portal":"CONTROL","status":"placeholder"})
