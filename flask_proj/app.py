###############################################################################
## JeoparDIY Flask Application  
## Team 2
##
## The **prefix.py** code is included to allow code to be developed within
## the **csel.io** environment.  There is a required prefix to be used when
## pages access the **csel.io** virtual machine from a local machine browser.
## 
###############################################################################

###############################################################################
## Import "prefix" code to make your app usable when running Flask either in 
## the csel.io virtual machine or running on a local machine.
## The module will create an app to use.
import prefix

from flask import Flask, url_for
from flask import render_template
from markupsafe import escape

# create app to use in this Flask application
app = Flask(__name__)

# Insert the wrapper for handling PROXY when using csel.io virtual machine
# Calling this routine will have no effect if running on local machine
# prefix.use_PrefixMiddleware(app)   

# test route to show prefix settings
@app.route('/prefix_url')  
def prefix_url():
    return 'The URL for this page is {}'.format(url_for('prefix_url'))

###############################################################################

# Define routes
@app.route('/')
def index():
    return render_template('index.html')

# Game instructions
@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/gameplay')
def gameplay(): # will need to send in categories somehow...
    return render_template('gameplay.html')



###############################################################################
# main driver function
if __name__ == '__main__':
    # run() method of Flask class runs the application 
    # on the local development server using port 3308 instead of port 5000.
    app.run(host='0.0.0.0', port=3308)

