#!/usr/bin/env python
# coding: utf-8

# ANS1

# In[11]:


get_ipython().system('pip install bokeh')


# In[12]:


import bokeh.io
import bokeh.plotting
bokeh.io.output_notebook()
from bokeh.plotting import figure , output_file, show
from bokeh.sampledata.iris import flowers
output_file('test.html')

p = figure(title = 'test flower')
p.xaxis.axis_label = "petal_length"
p.yaxis.axis_label = "petal_width"
p.circle(flowers['petal_length'] , flowers['petal_width'])
show(p)


# ANS2

# In[13]:


from bokeh.plotting import figure, output_file, show

# create a new plot with a title and axis labels
p = figure(title="My Plot", x_axis_label='X', y_axis_label='Y')

# add circles to the plot with x and y values
x = [1, 2, 3, 4, 5]
y = [6, 7, 2, 4, 5]
p.circle(x, y, size=10, color='blue')

# add squares to the plot with x and y values
x2 = [1.5, 2.5, 3.5, 4.5, 5.5]
y2 = [9, 8, 6, 2, 4]
p.square(x2, y2, size=10, color='red')

# save the plot to an HTML file and show it
output_file("myplot.html")
show(p)


# ANS3

# In[17]:



"""A Bokeh server is a Python application that provides a web-based interface for creating 
interactive plots and visualizations using Bokeh. It allows you to create web applications 
that can serve up interactive plots, which can be updated in real-time based on user input or external events."""

from bokeh.io import curdoc
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource
from bokeh.layouts import column
from bokeh.models.widgets import Button
import numpy as np

# create a data source with random x and y values
source = ColumnDataSource(data=dict(x=[], y=[]))

# create a scatter plot with the data source
p = figure()
p.circle(x='x', y='y', source=source)

# create a button widget that updates the plot
button = Button(label='Update Plot')

def update_plot():
    # generate new random x and y values
    x = np.random.rand(50)
    y = np.random.rand(50)
    source.data = dict(x=x, y=y)

button.on_click(update_plot)

# add the plot and button to the document
curdoc().add_root(column(p, button))


# ANS5

# In[18]:


from bokeh.plotting import figure
from bokeh.embed import server_document
from bokeh.server.server import Server
from flask import Flask, render_template

app = Flask(__name__)

def bokeh_app(doc):
    # create a scatter plot
    p = figure()
    p.circle([1, 2, 3], [4, 5, 6])
    
    # add the plot to the document
    doc.add_root(p)

# create a Bokeh server instance
bokeh_server = Server({'/bokeh': bokeh_app}, num_procs=1)

# start the server
bokeh_server.start()

@app.route('/')
def index():
    # get the Bokeh server URL
    bokeh_url = bokeh_server.urls['/bokeh']
    
    # render the Flask template with the Bokeh URL
    return render_template('index.html', bokeh_url=bokeh_url)

if __name__ == '__main__':
    app.run()

    
    
<!DOCTYPE html>
<html>
<head>
    <title>Bokeh Plot</title>
</head>
<body>
    <h1>Bokeh Plot</h1>
    <p>Here's a Bokeh plot:</p>
    <iframe src="{{ bokeh_url }}" width="600" height="400"></iframe>
</body>
</html>


# In[ ]:




