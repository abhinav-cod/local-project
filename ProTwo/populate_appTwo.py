import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ProTwo.settings')


import django
django.setup()

## FAKE PPOP SCRIPT
import random
from appTwo.models import AccessRecord,Webpage,Topic
from faker import Faker


fakegen = Faker()
topics = ['search','social','Marketplace','News','Games']

def add_topics():
    t=Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):

    for entry in range(N):
        top=add_topics()

        #create fake data
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

   #create a new webpage entry
        webpg = Webpage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]
 #create a fake access record for that Webpage
        acc_rec = AccessRecord.objects.get_or_create(name=webpg,date=fake_date)[0]



if __name__ == '__main__':
    print("populating script!")
    populate(20)
    print("populaating complete")
