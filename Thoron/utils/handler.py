from rest_framework import status
from rest_framework.views import exception_handler
from rest_framework.response import Response


def custom_handler(exc, context):
    response = exception_handler(exc, context)
    if response is not None:
        return Response(
                "Petición incorrecta o errónea. "
                "Revise los parámetros e intente de nuevo.",
                response.status_code)
    return response
