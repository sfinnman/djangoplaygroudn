from polls.models.user import User
from polls.renderers import users

def index(request):
  return users.render(User("Peter", 25))