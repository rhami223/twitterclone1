from django.db import models
from twitteruser.models import TwitterUser
from tweet.models import Tweets
#howard Post helped me with this project

class Notifications(models.Model):
    tweet_notify = models.ForeignKey(Tweets, on_delete=models.CASCADE)
    user_notify = models.ForeignKey(TwitterUser, on_delete=models.CASCADE)
    


# Create your models here.
