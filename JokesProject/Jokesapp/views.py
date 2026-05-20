from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
import requests


# Create your views he

class JokesDetails(APIView):

    def get(self, request,):
        jokes_get = requests.get("https://official-joke-api.appspot.com/jokes/random")
        response = jokes_get.json()
        context = {'setup':response['setup'],'punchline':response['punchline']}
        return render(request,'jokesapp/jokes.html',context)
