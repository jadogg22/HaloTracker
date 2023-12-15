from django.urls import path
from . import views

urlpatterns = [
    path('', view=views.index, name="index"),
    path("getUserData", view=views.get_user, name="get_user"),
    path("userData/<str:username>", view=views.get_stats_by_username, name="get_user_by_username"),
    path("getStats/", view=views.get_stats, name="get_stats")

]
