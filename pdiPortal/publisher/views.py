"""
This is the views for the publisher application.
"""

from django.contrib.admin.views.decorators import user_passes_test
from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import View

from rest_framework.generics import RetrieveAPIView
from rest_framework import permissions

from braces.views import LoginRequiredMixin, PermissionRequiredMixin

from .forms import CreateApplicationForm
from .models import Application
from .serializers import ApplicationSerializer

# Create your views here.
@login_required
def publisher(request):
    """This is the home page for the publisher. It shows the """
    user = request.user
    context = {'user': user}
    template = 'publisher/publisher.html'
    if user.is_publisher or user.is_superuser:
        return render(request, template, context)
    else:
        return redirect('dashboard')


class CreateApplication(LoginRequiredMixin,
                        PermissionRequiredMixin,
                        View):
    """Views required for application creation."""
    permission_required = "auth.add_Application"

    def get(self, request):
        """This shows the form for creating a new application"""
        user = request.user
        if user.is_publisher or user.is_superuser:
            app_form = CreateApplicationForm()
            context = {'user': user, 'appForm': app_form}
            template = 'publisher/create_application.html'
            return render(request, template, context)
        else:
            return redirect('dashboard')

    def post(self, request):
        """This will process the form when submitted."""
        application_form = CreateApplicationForm(request.POST, request.FILES)
        if application_form.is_valid():
            app = application_form.save()
            return redirect('publisher')
        else:
            return render_to_response('core/form-error.html', {'form': application_form})


class GetApplication(RetrieveAPIView):
    """This endpoint retireved an application by id."""

    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    lookup_field = '_id'
