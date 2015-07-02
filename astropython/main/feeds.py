from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
from .models import Tutorial

class RSSFeed(Feed):
    title = "Police beat site news"
    link = "feed/rss"
    description = "Updates on changes and additions to police beat central."

    def items(self):
        return Tutorial.objects.order_by('-created')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.body