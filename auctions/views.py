from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import User, Listing, comments, Watchlist, Bids
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

itemList = ['Fashion', 'Toys', 'Electronics', 'Home']

def index(request):
    listings = Listing.objects.filter(active=True)
    return render(request, "auctions/index.html",{
        "listings":listings
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")

@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

@login_required
def create(request):
    if request.method == "POST":
        title = request.POST["title"]
        description = request.POST["desc"]
        state = True
        person = request.user
        image = request.POST["img"]
        cat = request.POST["cat"]
        start_bid = request.POST["minbid"]
        item = Listing.objects.create(user=person, title=title,description=description,active=state,image=image,category=cat,starting_bid=start_bid)
        Bids.objects.create(listing = item, user=person, bid=start_bid, count=0)

        return HttpResponseRedirect(reverse("index"))
    return render(request, "auctions/create.html", {
        "categories":itemList
    })


def listin(request, id):
    listing = Listing.objects.get(pk=id)
    items = []
    if request.user.is_authenticated:
        watchlists = request.user.items.all()
        for i in watchlists:
            items.append(i.listing)
    comment = {}
    bidsin = Bids.objects.get(listing=listing)
    try:
        comment = comments.objects.filter(listing=listing)
    except:
        comment = {}
    return render(request, "auctions/listing.html", {
        "listing":listing,
        "watchlist" : items,
        "bids":bidsin,
        "comments" : comment
    })

@login_required
def watch(request):
    if request.method == "POST":
        id = request.POST['item']
        item = Listing.objects.get(pk=id)
        Watchlist.objects.create(user = request.user, listing = item)
        return HttpResponseRedirect(reverse("listing", args=[id]))
    watchlists = request.user.items.all()
    items = []
    for i in watchlists:
        items.append(i.listing)
    return render(request, "auctions/watchlist.html", {
        "items": items
    })

@login_required
def notwatch(request):
    id = request.POST['item']
    item = Listing.objects.get(pk=id)
    Watchlist.objects.filter(user = request.user, listing = item).delete()
    watchlists = request.user.items.all()
    items = []
    return HttpResponseRedirect(reverse("listing", args=[id]))

@login_required
def biding(request):
    if request.method == "POST":
        id = request.POST['item']
        item = Listing.objects.get(pk=id)
        person = request.user
        price = request.POST['price']
        # try:
        #     bidlist = Bids.objects.get(listing = item)
        # except:
        #     if int(price) < item.starting_bid:
        #         return render(request, "auctions/error.html")
        #     Bids.objects.create(listing = item, user=person, bid=price, count=1)
        # else:
        bidlist = Bids.objects.get(listing = item)
        if int(price) < bidlist.bid:
            return render(request, "auctions/error.html")
        Bids.objects.filter(listing = item).update(user=person,  bid=price, count=bidlist.count+1)
        Listing.objects.filter(id = id).update(starting_bid=price)
        return HttpResponseRedirect(reverse("listing", args=[id]))

@login_required   
def close(request):
    id = request.POST["ite"]
    Listing.objects.filter(pk = id).update(active=False)
    return HttpResponseRedirect(reverse("index"))

@login_required
def comment(request):
    if request.method == "POST":
        person = request.user
        id = request.POST["item"]
        item = Listing.objects.get(pk=id)
        text = request.POST["comment"]
        comments.objects.create(user = person, listing=item, comment=text)
        return HttpResponseRedirect(reverse("listing", args=[id]))

@login_required
def category(request):
        return render(request, "auctions/categories.html",{
                "items" : itemList
            })

@login_required
def categories(request, cat):
        items = Listing.objects.filter(category = cat, active=True)
        return render(request, "auctions/category.html",{
            "items" : items,
            "cat":cat
        })
    