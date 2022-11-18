from django.http import HttpResponseNotFound
from django.shortcuts import render

# Create your views here.
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView


class HelloWorld(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'hello.html'

    def get(self, request, *args, **kwargs):
        name = self.request.query_params.get("name", None)
        message = self.request.query_params.get("message", None)
        if name == None or message == None:
            return HttpResponseNotFound('You must input name and message!')
        return Response({'name': name, 'message': message})
