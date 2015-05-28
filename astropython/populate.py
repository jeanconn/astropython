import os
import json
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'astropython.settings')

import django
django.setup()

from tutorials.models import WYSIWYGTutorial,MarkdownTutorial,TutorialSeries
from blog.models import Event,MarkdownPost,WYSIWYGPost
from packages.models import MarkdownInput,WYSIWYGInput
from category.models import Category

def populate_tutorials():
    global base
    path_localdata=os.path.join(base,'Tutorials')
    try:
        no=len(os.walk(path_localdata).next()[2])
        for i in range(1,no+1):
            with open(path_localdata+"//"+str(i)+".json") as data_file:
                data=json.load(data_file)
                s=""
                for name in data:
                    if (name=='tags'):
                        s1=""
                        for items in data[name]:
                            s1=s1+","+str(items)
                            s=s1[1:]
                    else:
                        s=data[name]
                    if(name.encode('ascii','ignore')=='author'):
                        author=s.encode('ascii','ignore')
                    elif(name.encode('ascii','ignore')=='title'):
                        title=s.encode('ascii','ignore')
                    elif(name.encode('ascii','ignore')=='description'):
                        desc=s.encode('ascii','ignore')
                    elif(name.encode('ascii','ignore')=='tags'):
                        tags=s.encode('ascii','ignore')
                    elif(name.encode('ascii','ignore')=='date_published'):
                        date=s.encode('ascii','ignore')
                    #t=WYSIWYGTutorial.objects.get_or_create(category='Uncategorized')
                    t.save()
                    return t
    except IOError:
        print("IOError encountered!")

# Start execution here!
if __name__ == '__main__':
    _1orig_path=os.getcwd()
    _orig_path=os.path.dirname(_1orig_path)
    base=os.path.join(_orig_path,'ported_data')
    print "Starting Astropython population script..."
    opt=raw_input("Do you want to populate the tutorials? (y/n):")
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