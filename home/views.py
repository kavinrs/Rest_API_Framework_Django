from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

@api_view(['GET'])
def index(request):
    obj={
        'name':'kavin',
        'age':21,
        'place':'chennai'
    }
    return Response(obj)