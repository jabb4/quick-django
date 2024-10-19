from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout

import uuid

from .forms import *
from .models import User

from .validation.validate_username import testUsernameExistence
from .validation.validate_password import testCurrentPassword, testNewPassword

from .tasks import example_task

## This is an example view that tests the background task
def example(request):
    example_task.delay()
    return HttpResponse("Example page")

def login_view(request):
    page = "login"
    logged_in = request.user.is_authenticated
    user = request.user
    error_message = None
    success_message = None

    if logged_in:
        redirect("account")

    form = UserLoginForm

    try:
        if request.method == "POST" and request.POST["password"]:
            form = UserLoginForm(data=request.POST)
            print(form.errors)
            if form.is_valid():
                username = request.POST["username"]
                password = request.POST["password"]
                user = authenticate(request, username=username, password=password)
                if user:
                    login(request, user)
                    return redirect("account")
                else:
                    error_message = "Username OR Password is not correct"
    except KeyError:
        pass

    context = {
        "page": page, "error_message": error_message, "success_message": success_message,
        "form": form,
    }
    return render(request, "login.html", context=context)


def logout_view(request):
    page = "logout"
    logged_in = request.user.is_authenticated
    user = request.user
    error_message = None
    success_message = None

    if logged_in:
        logout(request)

    return redirect("login")

def register_view(request):
    page = "register"
    logged_in = request.user.is_authenticated
    user = request.user
    error_message = None
    success_message = None

    if logged_in:
        return redirect("account")

    form=CreateUserForm

    if request.method == "POST":
        try:
            if request.POST["username"] and request.POST["password1"] and request.POST["password2"]:
                form=CreateUserForm(request.POST)

                ### Check Username ###
                error_message = testUsernameExistence(
                    request=request, username=request.POST["username"])

                ### Check Password ###
                if not error_message:
                    error_message = testNewPassword(
                        request.POST["password1"], request.POST["password2"])

                if not error_message:
                    print("Creating user")
                    user = form.save()
                    user.save()
                    login(request, user)
                    return redirect("account")
        except KeyError:
            error_message = "Fill in all fields"

    context = {
        "page": page, "user": user, "logged_in": logged_in, "error_message": error_message, "success_message": success_message,
        "form":form, 
    }
    return render(request, "register.html", context=context)

def account_view(request):
    
    page = "account"
    user = request.user
    logged_in = user.is_authenticated
    error_message = None
    success_message = None

    if not logged_in:
        return redirect("login")

    delete_user_page = False
    form = None


### Check if method is POST ###
    if request.method == "POST":

### Delete User ###
        try:
            if request.POST["delete_user"]:
                page = "edit_user_child"
                delete_user_page = True
                form = DeleteUserForm
        except KeyError:
            pass
        try:
            if request.POST["delete_user_password"]:

                ### Check if password is current password ###
                error_message = testCurrentPassword(
                    request=request, password=request.POST["delete_user_password"])

                if error_message == None:

                    ### Deleting User ###
                    user.delete()
                    return redirect("login")

                else:
                    page = "edit_user_child"
                    delete_user_page = True
                    form = DeleteUserForm
        except KeyError:
            pass

    context = {
        "page": page, "user": user, "logged_in": logged_in, "error_message": error_message, "success_message": success_message,
        "form": form, "delete_user_page": delete_user_page
    }
    return render(request, "account.html", context=context)