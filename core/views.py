from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.views import View

from .models import Message


class HomeView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        messages = Message.objects.all()
        return render(request, "core/home.html", {"messages": messages})
