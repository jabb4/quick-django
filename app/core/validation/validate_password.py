from django.contrib.auth import authenticate

def testCurrentPassword(request, password):
    if not authenticate(request, username=request.user.username, password=password):
        return "Wrong Current Password"

def testNewPassword(password1, password2):

    alph_chars = "abcdefghijklmnopqrstuvwxyz"
    number_chars = "1234567890"
    special_chars = "!@#$%^&*"
    alph_chars_in_password = False
    number_chars_in_password = False
    special_chars_in_password = False

    for char in alph_chars:
        if char in password1:
            alph_chars_in_password = True
    if alph_chars_in_password == False:
        return "Password needs to include an alphabetic character (abcdefghijklmnopqrstuvwxyz)"

    for char in number_chars:
        if char in password1:
            number_chars_in_password = True
    if number_chars_in_password == False:
        return "Password needs to include a number character (1234567890)"

    for char in special_chars:
        if char in password1:
            special_chars_in_password = True
    if special_chars_in_password == False:
        return "Password needs to include a special character (!@#$%^&*)"

    if len(password1) < 8:
        return "Password length needs to be atleast 8"

    elif password1 != password2:
        return "Passwords dosent match"