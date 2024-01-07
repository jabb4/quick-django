from .validate_password import testCurrentPassword
from .validate_username import testUsernameExistence

def testEditUser(request, email, password):
    if testCurrentPassword(request=request, password=password):
        return testCurrentPassword(request=request, password=password)
    elif testUsernameExistence(request=request, email=email):
        return testUsernameExistence(request=request, email=email)
