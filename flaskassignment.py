#!/usr/bin/env python
# coding: utf-8

# ANS1

# In[1]:


"""GET:
The GET method is used to retrieve data from a server. When a GET request is made, 
the server responds with the requested data in the form of a web page, a JSON file, or
any other type of data. In Python, you can make a GET request using the requests library:

import requests

response = requests.get(url)


POST:
The POST method is used to send data to a server. When a POST request is made, 
the data is sent in the request body instead of the URL. In Python, you can make a POST request using the requests library:

import requests

response = requests.post(url, data=data)


"""


# ANS2

# In[2]:


"""Requests are used in Flask to handle incoming HTTP requests from clients and generate appropriate HTTP responses.

Flask is a web framework that allows you to build web applications in Python.
It provides tools and libraries for handling HTTP requests and responses, URL routing, and much more.

When a client sends an HTTP request to a Flask application, the request is
received by Flask and processed to determine what action should be taken. 
The request can contain various parameters, headers, and data that 
can be used by the Flask application to generate a response.

"""


# ANS3

# In[3]:


"""Requests are used in Flask to handle incoming HTTP requests from clients and generate appropriate HTTP responses.

Flask is a web framework that allows you to build web applications in Python. It provides tools and libraries for handling HTTP requests and responses, URL routing, and much more.

When a client sends an HTTP request to a Flask application, the request is received by Flask and processed to determine what action should be taken. The request can contain various parameters, headers, and data that can be used by the Flask application to generate a response.

Flask uses the requests library to handle incoming requests and provide a simple interface for working with HTTP requests and responses. The requests library allows Flask to parse incoming requests and extract information such as request headers, cookies, and form data.

Once the Flask application has processed the request and generated a response, the response is sent back to the client using the appropriate HTTP status code and headers.

In summary, the requests library is used in Flask to handle incoming HTTP requests and generate appropriate HTTP responses.




Study with masti
Why is redirect() used in Flask?
In Flask, the redirect() function is used to redirect a client to a different URL. It is often used to redirect users to a different page after they have completed an action, such as submitting a form.

There are several reasons why you might want to use redirect() in Flask:

Redirect after form submission: When a user submits a form on a website, it is common to redirect them to a different page. This can be done using the redirect() function. For example, if a user submits a login form, you might want to redirect them to their account page.

Redirect after authentication: When a user logs in to a website, you might want to redirect them to a different page. This can be done using the redirect() function. For example, if a user logs in to your website, you might want to redirect them to their account page.

Redirect to a new URL: If a page has moved to a new URL, you can use the redirect() function to automatically redirect users to the new URL. This can help prevent broken links and ensure that users can still find the content they are looking for."""


# ANS4

# In[4]:


"""Templates in Flask are files that contain HTML, CSS, 
and other content that is used to generate dynamic web pages. 
Templates allow you to separate the presentation of your web pages from the underlying business logic,
making it easier to maintain and update your code.

The render_template() function is used in Flask to render a template and return it as a response to an HTTP request.
The function takes the name of the template as its first argument, and any additional arguments are passed to the template context.

<!DOCTYPE html>
<html>
  <head>
    <title>Greeting</title>
  </head>
  <body>
    <h1>Hello, {{ name }}!</h1>
  </body>
</html>

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/greeting/<name>')
def greeting(name):
    return render_template('greeting.html', name=name)


"""


# ANS5

# In[ ]:





# In[7]:


from IPython import display
display.Image('s.png')


# In[ ]:




