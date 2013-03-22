db.messages.aggregate([
   {
      "$group":
      {
         "_id": { "from": "$headers.From" },
         "to_set" : { "$addToSet": "$headers.To" }
      }
   }
])

db.messages.find({"headers.Message-ID":"<8147308.1075851042335.JavaMail.evans@thyme>"})

db.messages.update({"headers.Message-ID":"<8147308.1075851042335.JavaMail.evans@thyme>"}, 
{"$push": {"headers.To": "mrpotatohead@10gen.com"}})

db.messages.aggregate([
   { "$unwind": "$headers.To"},
   {
      "$group":
      {
         "_id": { "to": "$headers.To", "from": "$headers.From" },
         "count": { "$sum" :1 }
      }
   },
   {
      "$sort": { "count": -1}
   },
   {
      "$limit": 5
   },
   {
      "$project" :
      {
         _id:0,
         "from" : '$_id',
         "count": 1
      }
   }
]);