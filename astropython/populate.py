"""
This script populated the database initially with the old ported data stored with the repo
"""
import os
import json
import datetime
import random
from slugify import slugify
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'astropython.settings')

#Setup Django and add all dependencies and code automatically
import django
django.setup()

from tutorials.models import Tutorial
from blog.models import Post
from packages.models import Package

from django.contrib.auth.models import User

"""
initialize() will be used to create Groups and other general entities in the future
"""
def initialize():
    pass

"""
Main population script that parses JSON and stores them in model objects and then to the database
"""
def populate(path_localdata,obj):
    author=""
    title=""
    desc=""
    date=""
    s=""
    typeObj=type(obj)#Find which type of model we are populating
    no=len(os.walk(path_localdata).next()[2])#find no. of json files in the directory
    for i in range(1,no+1):
        with open(path_localdata+"//"+str(i)+".json") as data_file:#open the json file
            data=json.load(data_file)#load data in python variable
            t=typeObj()#create a new object
            t.save()#initially save the empty object. This generates a primary key which is required to add any new properties
            for name in data:
                if (name=='tags'):
                    for items in data[name]:
                        s1=str(items)
                        t.tags.add(s1)#Add tags one by one.Note that this handles duplicate tags automatically
                else:
                    s=data[name]#Find the field
                    if(name=='author'):
                        author=s
                    elif(name=='title'):
                        title=s
                    elif(name=='description'):
                        desc=s
                    elif(name=='date_published'):
                        date=s
            t.title=title#Set the title
            t.body=desc#Add the body
            t.input_type="WYSIWYG"
            t.state="submitted"
            try:
                t.slug=slugify(title)#Generate slug
                t.save()#Save the current state
            except:
                t.slug=slugify(title)+str(random.randrange(1,10000000+1))#If 2 objects have same title,this prevents the same slug from being generated
            t.published=datetime.datetime.strptime(date,"%Y-%m-%d") #Add publishing date
            u=User.objects.get_or_create(username=author)#If user is absent, create user
            t.save()
            if(u[1]==True):
                u[0].save()#If the user is not present ,create it
            if(typeObj==type(Tutorial())):
                t.authors.add(u[0])
            else:
                t.authors=u[0]
            t.save()#save all elements
            print("Entered an element successfully!")

# Start execution here!
if __name__ == '__main__':
    _temp_orig_path=os.getcwd()
    _orig_path=os.path.dirname(_temp_orig_path)
    base=os.path.join(_orig_path,'ported_data/html')#Path to Json data
    initialize()
    #Take inputs
    print "Starting Astropython population script..."
    opt=raw_input("Do you want to populate the tutorials? (y/n):")
    if opt=='y':
        obj=Tutorial()
        populate(path_localdata=os.path.join(base,'Tutorials'),obj=obj)
    opt=raw_input("Do you want to populate the blogs? (y/n):")
    if opt=='y':
        obj=Post()
        populate(path_localdata=os.path.join(base,'Blogs'),obj=obj)
    opt=raw_input("Do you want to populate the packages? (y/n):")
    if opt=='y':
        obj=Package()
        populate(path_localdata=os.path.join(base,'Resources and Tools'),obj=obj)