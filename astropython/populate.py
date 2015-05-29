import os
import json
import datetime
from slugify import slugify
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'astropython.settings')

import django
django.setup()

from tutorials.models import WYSIWYGTutorial,MarkdownTutorial,TutorialSeries
from blog.models import Event,MarkdownPost,WYSIWYGPost
from packages.models import MarkdownInput,WYSIWYGInput
from category.models import Category

from django.contrib.auth.models import User

def initialize():
    pass
    #Use this to create groups and other general stuff in the future


def populate_tutorials():
    global base
    author=""
    title=""
    desc=""
    date=""
    s=""
    path_localdata=os.path.join(base,'Tutorials')
    try:
        no=len(os.walk(path_localdata).next()[2])
        for i in range(1,no+1):
            with open(path_localdata+"//"+str(i)+".json") as data_file:
                data=json.load(data_file)
                t=WYSIWYGTutorial()
                t.save()
                for name in data:
                    if (name=='tags'):
                        for items in data[name]:
                            s1=str(items)
                            t.tags.add(s1)
                    else:
                        s=data[name]
                        if(name=='author'):
                            author=s
                        elif(name=='title'):
                            title=s
                        elif(name=='description'):
                            desc=s
                        elif(name=='date_published'):
                            date=s
                #t=WYSIWYGTutorial(title=title,body=desc,slug=slugify(title))
                t.title=title
                t.body=desc
                t.slug=slugify(title)
                t.published=datetime.datetime.strptime(date,"%Y-%m-%d")
                u=User.objects.get_or_create(username=author)
                c=Category.objects.get_or_create(title='Uncategorized')
                t.save()
                if(u[1]==True):
                    u[0].save()
                if(c[1]==True):
                    c[0].save()
                t.authors.add(u[0])
                t.categories.add(c[0])
                t.save()
                print("Entered element!")
    except IOError:
        print("IOError encountered!")

# Start execution here!
if __name__ == '__main__':
    _temp_orig_path=os.getcwd()
    _orig_path=os.path.dirname(_temp_orig_path)
    base=os.path.join(_orig_path,'ported_data/html')
    print "Starting Astropython population script..."
    opt=raw_input("Do you want to populate the tutorials? (y/n):")
    initialize()
    if opt=='y':
        populate_tutorials()
    """
    opt=raw_input("Do you want to populate the blogs? (y/n):")
    if opt=='y':
        populate_blogs()
    opt=raw_input("Do you want to populate the packages? (y/n):")
    if opt=='y':
        populate_packages()
    opt=raw_input("Do you want to populate the code snippets? (y/n):")
    if opt=='y':
        populate_snippets()
    """