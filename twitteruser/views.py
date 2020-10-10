from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import TwitterUser
from tweet.helpers import get_tweets, user_tweets, get_user_tweets, get_tweet
from notification.helpers import count_notification, get_notification, delete_notification

#Howard Post helped me with this project
@login_required
def index_view(request):
    userinfo = TwitterUser.objects.get(id=request.user.id)
    followed_count = userinfo.followed.all().count()
    tweets = get_tweets(userinfo)
    count_tweet = user_tweets(userinfo)
    count_notify = count_notification(userinfo)
    return render(request, "index.html", {
        "title": "Twitter Clone",
        "userinfo": userinfo,
        "followed_count": followed_count,
        "tweets": tweets,
        "tweet_count": count_tweet,
        "notif_count": count_notify,
        "template_name": "tweets.html"
    })
def profile_view(request, user_username):
    userinfo = TwitterUser.objects.get(username=user_username)
    followed_count = userinfo.followed.all().count()
    tweets = get_user_tweets(userinfo)
    count_tweet = user_tweets(userinfo)
    count_notify = count_notification(userinfo)
    return render(request, "index.html", {
        "title": "Twitter Clone",
        "userinfo": userinfo,
        "followed_count": followed_count,
        "tweets": tweets,
        "tweet_count": count_tweet,
        "notif_count": count_notify,
        "template_name": "tweets.html"
    })
def tweet_view(request, tweet_id):
   
    tweets = get_tweet(tweet_id)
   
    return render(request, "index.html", {
        "title": "Twitter Clone",
        
        "tweets": tweets,
        
        "template_name": "tweets.html"
    })
@login_required
def notification_view(request, user_username):
    userinfo = TwitterUser.objects.get(username=user_username)
    followed_count = userinfo.followed.all().count()
    tweets = get_user_tweets(userinfo)
    count_tweet = user_tweets(userinfo)
    notif = get_notification(userinfo)
    delete_notification(userinfo)
    count_notify = count_notification(userinfo)
    return render(request, "index.html", {
        "title": "Twitter Clone",
        "userinfo": userinfo,
        "followed_count": followed_count,
        "tweets": tweets,
        "tweet_count": count_tweet,
        "notif_count": count_notify,
        "notifications": notif,
        "template_name": "notifications.html"
    })
@login_required
def follow_view(request, user_username):
    user = TwitterUser.objects.get(username=user_username)
    request.user.followed.add(user)
    return redirect('/' + user.username + '/')
@login_required
def unfollow_view(request, user_username):
    user = TwitterUser.objects.get(username=user_username)
    request.user.followed.remove(user)
    return redirect('/' + user.username + '/')
