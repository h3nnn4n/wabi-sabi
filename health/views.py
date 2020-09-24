from django.http import HttpResponse


def index(_request):
    return HttpResponse('ok')
