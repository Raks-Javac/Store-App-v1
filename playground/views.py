from django.shortcuts import render
from .tasks import *
import requests
from django.core.cache import cache
from django.views.decorators.cache import cache_page
from rest_framework.views import APIView
import logging

logger = logging.getLogger(__name__)


class HelloView(APIView):
    def get(self, request):
        try:
            logger.info('Calling httpbin')
            response = requests.get('https://httpbin.org/delay/2')
            logger.info('Received the response')
            data = response.json()       
        except requests.ConnectionError:
            logger.info('HTTPBIN IS offline the response')
        return render(request, 'hello.html', {'name':data})
