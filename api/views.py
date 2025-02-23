from django.shortcuts import render
from django.http.response import JsonResponse

# Create your views here.
def Main(request):
    return JsonResponse(data={"erro":False}, safe=False)