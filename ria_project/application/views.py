from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from rest_framework import viewsets
from .serializers import RequestSerializer
from . import models


class RequestViewSet(viewsets.ModelViewSet):
    queryset = models.Request.objects.all()
    serializer_class = RequestSerializer


class RequestCreate(CreateView):
    model = models.Request
    fields = '__all__'


class RequestUpdate(UpdateView):
    model = models.Request
    fields = '__all__'
    success_url = reverse_lazy('index')


