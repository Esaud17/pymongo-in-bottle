<!DOCTYPE html>
<html>
   <head>
      <title>Hello World Template</title>
   </head>
   <body>
      <p>Welcome {{username}}<p>
      <ul>
         %for thing in things:
            <li>{{thing}}</li>
         %end
      </ul>
      <p>
      <form action="/favorite-fruit" method="POST">
         What is your favorite fruit?
         <input type="text" name="fruit" size="40" value=""><br>
         <input type="submit" value="Submit"><br>
      </form>
   </body>
</html>