from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User, Catagory, Listing, Comment, Bid 


def index(request):
    return render(request, "auctions/index.html", {"listings": Listing.objects.all(), "comments": Comment.objects.all()})

@login_required
def auction(request, listing_id):
    listing = Listing.objects.get(pk=listing_id)
    if request.method == "POST":
        action = request.POST.get("action")
        if action == "Bid":
            amount = int(request.POST.get("amount"))
            listing.current_price = amount
            listing.save()
            Bid.objects.create(
                creator = request.user,
                listing = listing,
                value = amount
            )
        elif action == "Comment":
            Comment.objects.create(
                contents = request.POST.get("content"),
                listing = listing,
                creator = request.user)
        elif action == "Close":
            highest_bid = Bid.objects.filter(listing=listing).order_by('-value').first()
            if highest_bid:
                listing.winner = highest_bid.creator  
            listing.active = False
            listing.save()
        elif action == "Add":
            listing.watchlist = True
            listing.save()
        elif action == "Remove":
            listing.watchlist = False
            listing.save()
    comments = Comment.objects.filter(listing=listing_id)
    bid = Bid.objects.filter(listing=listing_id)
    if request.user == listing.creator:
        owner = True
    else:
        owner = False
    return render(request, "auctions/auction.html" ,{"listing": listing, "comments": comments, "bid": bid, "owner": owner})

def listing(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        starting_bid = request.POST.get("starting_bid")
        current_price = request.POST.get("starting_bid")
        catagory = request.POST.get("catagory")
        image_url = request.POST.get("image_url") or ""

        catagories = Catagory.choices

        if not title or not starting_bid or not catagory:
            return render(request, "auctions/listing.html",{"error": "Please fill out the required fields", "catagories": catagories})
        
        try:
            starting_bid = int(starting_bid)
        except ValueError:
            return render(request, "auctions/listing.html", {
                "error": "Starting bid must be a number.",
                "catagories": catagories
            })

        listing = Listing(
            title = title,
            description = description,
            starting_bid = starting_bid,
            catagory = catagory,
            current_price = current_price,
            image_url = image_url,
            creator = request.user
        )

        listing.save()

        return HttpResponseRedirect(reverse("index"))

    catagories = Catagory.choices
    return render(request, "auctions/listing.html", {"catagories": catagories})

def watchlist(request):
    listing = Listing.objects.filter(watchlist = True)
    return render(request, "auctions/watchlist.html", {"listings": listing})

def catagories(request):
    selected = request.GET.get("catagory")
    if selected:
        listings = Listing.objects.filter(catagory=selected)
    else:
        listings = Listing.objects.all()
    return render(request, "auctions/catagories.html", {"Catagory": Catagory, "listings": listings, "selected": selected})

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

