from django.contrib.auth import authenticate

def testCurrentPassword(request, password):
    if not authenticate(request, username=request.user.username, password=password):
        return "Wrong Current Password"

def testNewPassword(password1, password2):

    if len(password1) < 15:
        return "Password length needs to be atleast 15"

    elif password1 != password2:
        return "Passwords dosent match"