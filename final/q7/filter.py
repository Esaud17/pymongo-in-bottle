import bottle

import pymongo
import cgi
import re
import datetime
import random
import hmac
import user
import sys

connection_string = "mongodb://localhost"
TOTAL = 100000
 
def remove_orphan():
    images_array = []
    for i in range(TOTAL):
       images_array.append(0)
    
    connection = pymongo.Connection(connection_string, safe=True)
    db = connection.blog
    albums = db.albums
    
    cursor = albums.find()
    
    for album in cursor:
       ilist = album["images"]
       for i in ilist:
          images_array[i] = 1

    delete_images(db, images_array)


def delete_images(db,list):
    images = db.images
    
    num = 0;
    for i in range(len(list)):
        if list[i] != 1:
           images.remove({'_id':i})
           num += 1
           print "Deleted image _id:%d" % i
    
    print "Total = %d" % num


remove_orphan()