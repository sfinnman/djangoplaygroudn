from django.http import HttpResponse
import json

def render(user):
  print(vars(user))
  return HttpResponse(json.dumps(vars(user)))