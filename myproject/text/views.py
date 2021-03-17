# from django.shortcuts import render
import re
# from django.http import HttpResponse
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
from .apps import textConfig
from rest_framework.views import APIView
from django.http import JsonResponse

class myprojectApiView(APIView):

    def post(self, request, format=None):
        """Handle HTML POST request"""
        request_content=request.data("name")
        name1=textConfig.request_content
        ph=re.findall('[0-9]+',name1)
        return JsonResponse(ph)
