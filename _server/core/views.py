from django.shortcuts import render
from django.conf  import settings
import json
import os
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from registration.models import UserProfile
from core.models import GameStats
from . import webScraper
import sqlite3

# Load manifest when server launches
MANIFEST = {}
if not settings.DEBUG:
    f = open(f"{settings.BASE_DIR}/core/static/manifest.json")
    MANIFEST = json.load(f)

# Create your views here.
@login_required
def index(req):
    context = {
        "asset_url": os.environ.get("ASSET_URL", ""),
        "debug": settings.DEBUG,
        "manifest": MANIFEST,
        "js_file": "" if settings.DEBUG else MANIFEST["src/main.ts"]["file"],
        "css_file": "" if settings.DEBUG else MANIFEST["src/main.ts"]["css"][0],
    }

    return render(req, "core/index.html", context)


def get_user(req):
    if req.user.is_authenticated:
        info = {
            "username": req.user.username,
            "first_name": req.user.first_name,
            "last_name": req.user.last_name,
            "email": req.user.email,
            "haloUsername": req.user.userprofile.haloUsername,
        }
        return JsonResponse(info)
    else:
        return JsonResponse({"user": None})

def get_user_by_username(req, username):
    user_info = UserProfile.objects.get(username=username)

    print(user_info)
    return JsonResponse(user_info)

def get_stats(req):
    print("calling function")
    stats = webScraper.getStats("jadogg22")
    return JsonResponse(stats)

def scrapeData(username):
    scrapStats = webScraper.getStats(username)
    if scrapStats == False:
        return JsonResponse({"notFound": True})
    stats = GameStats.create_from_dict(scrapStats)
    stats.save()
    stats.notFound = False
    stats = stats.to_dict()

    return stats

def get_stats_by_username(req, username):
    
    #search database for recent stats
    stats = GameStats.get_stats_by_username(username)

    if stats:
        print("Newest Gamestat:")
        if stats.isRecent():
            stats = stats.to_dict()
            return JsonResponse(stats) 
        else: 
            # not new enough
            stats = scrapeData(username)
            return JsonResponse(stats)


    else:
        print("couldn't find ya")
        stats = scrapeData(username)
        return JsonResponse(stats)


    #We want to store our own data in a database,
    #so the proper thing to do would be to 

    
    #check database for username
    #if username exists, and the last scrape was less then 3 hours return stats
    #else scrape the data and return stats


def get_user_debug(req):
     info = {
            "username": "testUser@test.com",
            "first_name": "jaden",
            "last_name": "anderson",
            "Email": "testUser@test.com",          
            "haloUsername": "XboxUsername",
            "Stats": {
                "kills": "12",
                "deaths": "15",
            }
        }
     return JsonResponse(info)


