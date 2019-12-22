from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.views import APIView
import json


@api_view(['GET', 'POST'])
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


class Pinger(APIView):

    def get(self, request, format=None):
        return HttpResponse("Get Request")

