from django.http import HttpResponse


def home_view(request):
    return HttpResponse("Hello, this is the home view of the Django project!")
