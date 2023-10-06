
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

class IndexView(View):
    def get(self, request):
        return render(request, 'topkalaAdmin/index.html')

class Index2View(View):
    def get(self, request):
        return render(request, 'topkalaAdmin/index2.html')

class StarterView(View):
    def get(self, request):
        return render(request, 'topkalaAdmin/starter.html')
