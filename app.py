import sys

from django.conf import settings
from django.urls import re_path
from django.http import HttpResponse

import logging

logger = logging.getLogger(__name__)

settings.configure(
    DEBUG=True,  # For debugging
    ALLOWED_HOSTS=['*'],
    SECRET_KEY="a-bad-secret",
    ROOT_URLCONF=__name__,
)


def home(request):
    params = [f"{key}={value}" for key, value in request.GET.lists()]
    information_to_print = f"Method: {request.method}\nPath: {request.path}\nQuery params: {params}\nBody: {request.body}"
    print(information_to_print)
    return HttpResponse(information_to_print.replace("\n", "<br>"))


urlpatterns = [
    # Match everything that is sent
    re_path(".*", home),
]

if __name__ == "__main__":
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)