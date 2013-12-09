whisky-time
===========

9th December 2013 - A Gentle Introduction to Web Apps...


Challenge
---------

Create a web application to calculate the cooking time for a Christmas turkey.

## Specs

* Your application should take the weight in kg from the path given to the web application, and return the cooking time in plain text. e.g. visiting <http://localhost:8000/5.25> in your browser should return:

  ```
  X hours YY minutes
  ```
  
* Use the following to calculate cooking time - these are base on [NHS guidelines for turkey cooking time][NHS] but having fixed the "gotchas" contained therein (if you finish early, see how many you can find there!):

  * allow 45 minutes per kg plus 20 minutes for a turkey under 4.5kg
  * allow 40 minutes per kg plus 20 minutes for a turkey of 4.5kg or more but less than 6.5kg
  * allow 35 minutes per kg plus 20 minutes for a turkey of 6.5kg or more

* Your application should comply with [PEP 333][PEP333] - [WSGI][WSGI], pronounced "whisky"
* Use ONLY The Python standard library - DO NOT use a Python web-framework to achieve the task

  (doing the task without a framework will give you a better understanding of how some of the frameworks operate if you need to use them in future)


## Hints

* The built-in [`wsgiref`][wsgiref] module is your friend!


## Solution

You're surely not expecting me to give you that just yet! I'll try to make available by about 19:30.


## Extra credit

* Write a web app that performs a task from a previous PyPool:

  * Love calculator
  * Roman numeral conversion - [Roman to Arabic](https://gist.github.com/bloomonkey/5754968) or Arabic to Roman

* Run your WSGI app under another framwework's web server (e.g. [CherryPy][CherryPy], [Tornado][Tornado]) - these are probably more suitable for production use than the server provided by [`wsgiref`][wsgiref]!


   [NHS]: http://www.nhs.uk/Livewell/Healthychristmas/Pages/cooking-turkey.aspx#cooking
   [PEP333]: http://www.python.org/dev/peps/pep-0333/ "PEP-0333 Python Web Server Gateway Interface"
   [WSGI]: http://wsgi.org
   [wsgiref]: http://docs.python.org/2/library/wsgiref.html
   [CherryPy]: http://docs.cherrypy.org/stable/refman/wsgiserver/init.html
   [tornado]: http://www.tornadoweb.org/en/stable/wsgi.html#wsgicontainer
