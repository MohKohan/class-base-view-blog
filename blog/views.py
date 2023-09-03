from django.shortcuts import render
from rest_framework import viewsets
from blog.models import SightseeingPlaces
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from blog.serializers import SightseeingPlacesSerializer,CategorySerializer

class project(ListView):
    queryset = SightseeingPlaces.objects.all()
    template_name = 'project.html'
    context_object_name = "projects"

class projectDetail(DetailView):
    model = SightseeingPlaces
    template_name = 'project-detail.html'
    context_object_name = "project"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    

class sightseeingPlacesViewSet(viewsets.ModelViewSet):
    queryset=SightseeingPlaces.objects.all()
    serializer_class = SightseeingPlacesSerializer







