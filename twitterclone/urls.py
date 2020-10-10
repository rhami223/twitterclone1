"""twitterclone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#Howard Post helped me with this project
from django.contrib import admin
from django.urls import path

from authentication import views as authviews
from tweet import views as tweetviews
from twitteruser import views as profileviews
urlpatterns = [
    path('', profileviews.index_view, name="home"),
    path('addtweet/', tweetviews.addtweet_view),
    path('notifications/<str:user_username>/', profileviews.notification_view),
    path('tweet_detail/<int:tweet_id>/', profileviews.tweet_view),
    path('login/', authviews.login_view),
    path('signup/', authviews.signup_view),
    path('logout/', authviews.logout_view),
    path('admin/', admin.site.urls),
    path('<str:user_username>/', profileviews.profile_view),
    path('<str:user_username>/follow/', profileviews.follow_view),
    path('<str:user_username>/unfollow/', profileviews.unfollow_view),
]