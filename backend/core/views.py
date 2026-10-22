# backend/core/views.py
# A "view" receives a request and returns a response.
# It replaces a Java @RestController method.

from rest_framework.decorators import api_view  # marks a function as an API
from rest_framework.response import Response    # builds the JSON reply


# @api_view(["GET"]) = this API accepts ONLY the GET action.
# Other actions (POST, DELETE...) get automatic error 405.
@api_view(["GET"])
def health(request):
    # Response() turns this Python dictionary into JSON
    return Response({"status": "ok", "app": "WorkMate"})