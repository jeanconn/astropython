import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'astropython.settings')

import django
django.setup()

from tutorials.models import WYSIWYGTutorial,MarkdownTutorial,TutorialSeries
from blog.models import Event,MarkdownPost,WYSIWYGPost
from packages.models import MarkdownInput,WYSIWYGInput
from category.models import Category

def populate():

def add_tutorial(cat, title, author):
    t = WYSIWYGTutorial.objects.get_or_create(category='Uncategorized', title=title,)[0]
    t.save()
    return t

# Start execution here!
if __name__ == '__main__':
    print "Starting Astropython population script..."
    populate()