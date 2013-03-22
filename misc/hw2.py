import sys
import pymongo

connection = pymongo.Connection('localhost', 27017)
db = connection.school
scores = db.scores

def find_one():
   print "Calling find_one()..."
   query = { 'student_id':10 }
   
   try:
      doc = scores.find_one(query)
   except:
      print "Unexpected error:", sys.exc_info()[0]
      
   print doc
   
def find():
   print "Calling find()..."
   query = { 'type':'exam' }
   
   try:
      cursor = scores.find(query)
   except:
      print "Unexpected error:", sys.exc_info()[0]
      
   for doc in cursor:
      print doc
   
def find_with_selector():
   print "Calling find()..."
   query = { 'type':'exam' }
   selector = { 'student_id': 1, '_id': 0 }
   
   try:
      cursor = scores.find(query, selector)
   except:
      print "Unexpected error:", sys.exc_info()[0]
      
   for doc in cursor:
      print doc
      
def find_with_gt():
   print "Calling find_with_gt()..."
   query = { 'type':'homework' }
   selector = { 'student_id': 1, '_id': 0 }
   
   try:
      cursor = scores.find(query).sort({ 'score': 1 }).limit(30)
   except:
      print "Unexpected error:", sys.exc_info()[0]
      
   for doc in cursor:
      print doc