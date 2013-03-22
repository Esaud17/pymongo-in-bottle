import sys
import pymongo

connection = pymongo.Connection('localhost', 27017)
db = connection.students
grades = db.grades

def find():
   print "Calling find()..."
   query = { 'type':'homework' }
   
   try:
      cursor = grades.find(query).sort([('student_id', 1 )])
   except:
      print "Unexpected error:", sys.exc_info()[0]

   students = []
   for doc in cursor:
      if doc['student_id'] in students:
         continue
      else:
         students.append(doc['student_id'])
         print "Deleting ", doc['_id']
         grades.remove({ '_id' : doc['_id'] })
      
   print "Total students:", len(students)
   
find()