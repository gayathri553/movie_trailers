#Movie Trailer

Udacity FullStack Nanodegree Course project-1
This project demonstrate the object class in python to determine the webpage.To do this project I used the HTML,CSS,Js code.
Inbulit bootstrap css is also used to do this project.

In this project floder I had mainly three files such as:
  -entertainment_center.py
  -media.py
  -fresh_tomatoes.py
 Mainly We must ensure that all these three flies should be in the same floder named as cgi-bin.
 
#entertainment_center.py:
  - This file consists of media and fresh_tomatoes which I are get through import.
  - It has the Movie class for that  I will create instances which can take three arguments(movie title,poster image url,trailer url).
  - Later I created a list which stores all the instances of the class.
  - Then I call the function named open_movies_page() which is in the fresh_tomatoes.py file.
#media.py
  -This file consists of class named Movie which has the init function that intialize the object to that class.
  -init function takes the parameters and local variable to refer the parameters.
  -This file also consists of another function named show_trailer which takes local parameter and has the  webbrowser open method to open 
   trailer url.
#fresh_tomatoes.py
  - In this file, firstly we should import webbrowser,os.
    Webbrowser is used to open the project in webpage and os is used for doing file operations.
  - Then I had three variables:
      -main_head:which consists of the head part of our html code.
      -main_content:which consists of body part.
      -main_title_content: consists of trailer part in youtube.
 #create_movie function:
   - which uses loop that takes all the movies that we had.
 #open_movies_page function:
   -which open the fresh_tomatoes.html page in browser
   -url path that we want to open the in browser.
   
 #To run this file:
    - I had  installed python
    - I had installed  GitBash
    - In that git Bash I had run some commands:
          - git init
          - git clone(which takes url that available in git resporitrary)
          - git status
          - git add -all
          - git commit -m "adding"
          - git push origin master.
          
  
