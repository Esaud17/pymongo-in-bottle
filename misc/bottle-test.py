'''
Created on Jan 27, 2013

@author: saung
'''
import bottle

@bottle.route('/')
def home_page():
   mythings = ['apple', 'banana', 'orange']
   return bottle.template("hello_world", {
                                             'username':"Sithu",
                                             'things': mythings
                                          })

@bottle.route('/testpage')
def test_page():
   return "This is a test page"


@bottle.post('/favorite-fruit')
def favorite_fruit():
   fruit = bottle.request.forms.get("fruit")
   if (fruit == None or fruit == ""):
      fruit = "No fruit selected"
   
   bottle.response.set_cookie("fruit", fruit)
   bottle.redirect('/show_fruit')


@bottle.route('/show_fruit')
def show_fruit():
   fruit = bottle.request.get_cookie("fruit")

   return bottle.template('fruit_selection.tpl', {'fruit': fruit})

   
   
bottle.debug(True)
bottle.run(host='localhost', port=8080, reloader=True)


