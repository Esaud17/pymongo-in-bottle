#!/usr/bin/env python
# encoding: utf-8
"""
remove-lowest-hw.py
Homework 3 - 1
"""
import sys
import pymongo

connection = pymongo.Connection('localhost', 27017, safe=True)
db = connection.school
students = db.students

def remove_lowest_hw():
	print "Calling remove_lowest_hw()..."
	# Find Minimum homework scores
	# NOTE: The '$unwind' section must be FIRST in the array
	query = [ 
		{ "$unwind": "$scores" },
		{ "$match" : {'scores.type':'homework'} },
		{ "$group": { '_id': { 'sid': '$_id', 'type':'$scores.type'}, 'minScore': {'$min': "$scores.score" }}}
		]

	try:
		cursor = students.aggregate(query)
		
		# Remove minimum homework scores
		print "Number of records found - ", len(cursor['result'])
		for doc in cursor['result']:
			print doc
			students.update({'_id': doc['_id']['sid'], 'scores.type' : 'homework'},
				{ '$pull':{ 'scores' : { 'score' : doc['minScore']} } })
	except:
		print "Unexpected error:", sys.exc_info()[0]
	

def main():
	remove_lowest_hw()

if __name__ == '__main__':
	main()

