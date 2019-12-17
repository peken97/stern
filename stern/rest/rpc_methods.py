from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.views import APIView
import json

def train():
    return HttpResponse("Invoked Train")

rpc_mapper = {
    'train': train
}


@api_view(['POST'])
def rpc_request_handler(request):
    print(request.data["method"])
    method = request.data["method"]
    return rpc_mapper[method]()

    
