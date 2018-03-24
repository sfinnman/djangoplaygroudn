from django.urls import path
from .controllers import users

urlpatterns = [
  path('users/', users.index, name='users')
]