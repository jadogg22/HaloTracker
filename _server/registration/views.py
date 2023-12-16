from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.http import JsonResponse
from .models import UserProfile

# Create your views here.
def sign_up(req):
    if req.method == "POST":
        user = User.objects.create_user(
            username=req.POST.get("email"),
            password=req.POST.get("password"),
            email=req.POST.get("email"),
            first_name=req.POST.get("first_name"),
            last_name=req.POST.get("last_name"),
        )
        if "haloName" not in req.POST:
            print("Halo Username is required")
            return JsonResponse({"error": "Halo Username is required"})
            
        user_profile = UserProfile(user=user, haloUsername=req.POST.get("haloName"))
        user_profile.save()
        login(req, user)
        context = {"user": user_profile}
        return redirect("/", context)
    else:
        return render(req, "registration/sign_up.html")

def sign_in(req):
    if req.method == "POST":
        user = authenticate(req, username=req.POST.get("email"), password=req.POST.get("password"))
        if user is not None:
            login(req, user)
            return redirect("/")

        return render(req, "registration/sign_in.html")
    else:
        return render(req, "registration/sign_in.html")

def logout_view(request):
    logout(request)
    return redirect(request, "registration/sign_in.html")

def delete_account(req):
    user = User.objects.get(id=req.user.id)
    user.delete()
    return redirect("registration/sign_in.html")