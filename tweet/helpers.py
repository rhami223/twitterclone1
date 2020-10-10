from .models import Tweets
from twitteruser.models import TwitterUser
from notification.models import Notifications
import re
def parse_tweet(tweet):
    pattern = re.compile(r'(@)(\w+)(\s|$)')
    match_found = pattern.search(tweet.text)
    if match_found:
        username = match_found.group(2)
        user = TwitterUser.objects.get(username=username)
        if user:
            Notifications.objects.create(
                tweet_notify=tweet,
                user_notify=user
            )
            return True
    return False
def get_tweets(userinfo):
    user_list = [userinfo.id]
    for u in userinfo.followed.all():
        user_list.append(u.id)
    tweets = Tweets.objects.filter(
        user__id__in=user_list).order_by('-posted_on')
    return tweets
def user_tweets(userinfo):
    return Tweets.objects.filter(user__id=userinfo.id).count()
def get_user_tweets(userinfo):
    return Tweets.objects.filter(user__id=userinfo.id).order_by('-posted_on')
def get_tweet(tweet_id):
    return Tweets.objects.filter(id=tweet_id)