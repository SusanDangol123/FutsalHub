from django.shortcuts import redirect
from futsalhubapp.models import User,Player
from django.contrib import messages

class Authenticate:
    def valid_user(function):
        def wrap(request):
            try:

                User.objects.get(email=request.session['email'])
                User.objects.get(password=request.session['password'])
                return function(request)

            except:
                messages.warning(request,"Password or Email error")
                return redirect("/login")

        return wrap


    def valid_player(function):
        def wrap(request):
           # print(request.session['email'])
            try:
                Player.objects.get(email=request.session['email'])
                Player.objects.get(password=request.session['password'])
                return function(request)

            except:
                messages.warning(request,"Password or Email error")
                return redirect("/login")

        return wrap
