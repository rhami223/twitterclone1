from django.shortcuts import render, HttpResponseRedirect,reverse
from django.contrib.auth.decorators import login_required
from .forms import AddTweetForm
from .models import Tweets
from .helpers import parse_tweet
#Howard Post helped me with this project

@login_required
def addtweet_view(request):
    if request.method == 'POST':
        form = AddTweetForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            tweet = Tweets.objects.create(
                text = data.get('text'),
                user = request.user
            )
            parse_tweet(tweet)
            return HttpResponseRedirect(reverse('home'))
    form = AddTweetForm()
    return render(request, 'generic_form.html', {'form': form})
    """
    docstring
    """
    pass


# Create your views here.
