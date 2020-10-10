from .models import Notifications
def count_notification(userinfo):
    return Notifications.objects.filter(
        user_notify=userinfo).count()
def get_notification(userinfo):
    notif = []
    notifications = Notifications.objects.filter(
        user_notify=userinfo)
    for n in notifications:
        notif.append(
            n.tweet_notify.user.username + '-' + n.tweet_notify.text)
    return notif
def delete_notification(userinfo):
    notifications = Notifications.objects.filter(
        user_notify=userinfo).delete()
    