from django.shortcuts import render, redirect
from futsalhubapp.forms import UserForm, PlayerForm
from futsalhubapp.models import User, Player
from django.http import HttpResponse, JsonResponse

from futsalhubapp.authenticate import Authenticate


def home(request):
    return render(request, "futsalhubapp/home.html")


def balaju(request):
    return render(request, "futsalhubapp/balaju.html")


def thamel(request):
    return render(request, "futsalhubapp/thamel.html")


def dillizabazar(request):
    return render(request, "futsalhubapp/dillizabazar.html")


def thimi(request):
    return render(request, "futsalhubapp/thimi.html")


def suryabinayak(request):
    return render(request, "futsalhubapp/suryabinayak.html")


def changunarayan(request):
    return render(request, "futsalhubapp/changunarayan.html")


def jawalakhel(request):
    return render(request, "futsalhubapp/jawalakhel.html")


def patan(request):
    return render(request, "futsalhubapp/patan.html")


def kumaripati(request):
    return render(request, "futsalhubapp/kumaripati.html")


def search(request):
    users = User.objects.filter(email__contains=request.GET['search'])[0:3].values()
    return JsonResponse(list(users), safe=False)


# Admin signup
def create(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("/")
            except:
                pass

    form = UserForm()
    return render(request, "futsalhubapp/create.html", {'form': form})


def edit(request, id):
    user = User.objects.get(id=id)
    return render(request, "futsalhubapp/edit.html", {'user': user})


def update(request, id):
    user = User.objects.get(id=id)
    form = UserForm(request.POST, instance=user)
    form.save()
    return redirect("/")


def delete(request, id):
    user = User.objects.get(id=id)
    user.delete()
    return redirect("/")


def adminLogin(request):
    return render(request, "futsalhubapp/AdminLogin.html")


def entry(request):
    request.session['email'] = request.POST['email']
    request.session['password'] = request.POST['password']
    return redirect('/home')


# @Authenticate.valid_user
def show(request):
    limit = 3
    page = 1
    if request.method == "POST":
        if "next" in request.POST:
            page = (int(request.POST['page']) + 1)

        elif "prev" in request.POST:
            page = (int(request.POST['page']) - 1)

        tempoffset = page - 1
        offset = tempoffset * page
        users = User.objects.raw("Select * from user limit 3 offset %s", [offset])

    else:
        users = User.objects.raw("Select * from user limit 3 offset 0")
    return render(request, "futsalhubapp/show.html", {'users': users, 'page': page})


# for player
def signup(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        repassword = request.POST['repassword']

        if password == repassword:
            if Player.objects.filter(username=username).exists():
                messages.info(request, "username already exist")
                return redirect('signup')
            elif Player.objects.filter(email=email).exists():
                messages.info(request, "email already taken")
                return redirect('signup')
            else:
                playerinfo = Player(fname=fname, lname=lname, username=username, email=email,
                                    password=password, repassword=repassword)
                playerinfo.save()
                print("new player created")
                return redirect('/')
        else:
            messages.info(request, "password not matching")
            return redirect('signup')
        return redirect('/')
    else:
        return render(request, "futsalhubapp/signup.html")


def login(request):
    return render(request, "futsalhubapp/login.html")


def entryCustomer(request):
    request.session['email'] = request.POST['email']
    request.session['password'] = request.POST['password']
    return redirect('/training')


@Authenticate.valid_player
def training(request):
    player = Player.objects.all()
    return render(request, "futsalhubapp/training.html", {'Player': player})


def showCustomer(request):
    limit = 3
    page = 1
    if request.method == "POST":
        if "next" in request.POST:
            page = (int(request.POST['page']) + 1)

        elif "prev" in request.POST:
            page = (int(request.POST['page']) - 1)

        tempoffset = page - 1
        offset = tempoffset * page
        players = Player.objects.raw("Select * from Player limit 3 offset %s", [offset])

    else:
        players = Player.objects.raw("Select * from Player limit 3 offset 0")
    return render(request, "futsalhubapp/showCustomer.html", {'players': players, 'page': page})


def dashboard(request):
    return render(request, "futsalhubapp/dashboard.html")
