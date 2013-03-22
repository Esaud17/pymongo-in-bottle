import json
import urllib2
import pymongo
import sys

connection = pymongo.Connection('localhost', 27017, safe=True)
db = connection.reddit
stories = db.stories

def load_reddit_json():
   reddit_page = urllib2.urlopen("http://www.reddit.com/r/technology/.json")
   parsed = json.loads(reddit_page.read())

   for item in parsed['data']['children']:
      stories.insert(item['data'])
   
def find_by_regex():
   print "Running query..."
   query = { 'title': {'$regex':'iOS'} }
   selector = { 'title': 1, '_id': 0 }
   
   try:
      cursor = stories.find(query, selector);
   except:
      print "Error:", sys.exc_info()[0]
      
   for doc in cursor:
      print doc
   
def find_by_dot():
   print "Running dot query..."
   query = { 'media_oembed.type': 'video' }
   projection = { 'media.oembed.url': 1, '_id': 0 }
   
   try:
      cursor = stories.find(query, projection);
   except:
      print "Error:", sys.exc_info()[0]
      
   for doc in cursor:
      print doc

   
if __name__ == "__main__":
   find_by_dot()
