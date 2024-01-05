from ..models import User


def testUsernameExistence(request, username):
    try:
        if str(request.user) != "AnonymousUser":
            if request.user.username == username:
                return None
        if User.objects.get(username=username):
            return "Email is taken"
    except:
        return None
