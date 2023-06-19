#Q1. What is Flask Framework? What are the advantages of Flask Framework?
""" 
Flask is a lightweight web framework written in Python. 
It is designed to be simple and easy to use, yet flexible enough to handle a wide range of web applications. 
Flask follows the WSGI (Web Server Gateway Interface) standard and is built on top of the Werkzeug toolkit and the Jinja2 template engine.
"""
""" 
Advantages of Flask Framework:

1.Lightweight and Minimalistic: Flask has a small core and only includes the essential features, 
allowing developers to have more control and flexibility in building their applications. It does 
not impose any specific project structure, making it easy to start and customize as per requirements.

2.Easy to Get Started: Flask has a simple and intuitive API, making it easy for beginners to learn 
and start building web applications. It provides clear and concise documentation with a large and 
supportive community.

3.Flexible and Extensible: Flask provides a wide range of extensions that can be added as needed, 
such as database integration, form validation, authentication, and more. These extensions help in 
extending the functionality of the framework without bloating the core.

4.Templating Engine: Flask uses the Jinja2 templating engine, which offers powerful and flexible 
templates for rendering dynamic content. It allows for easy separation of logic and presentation, 
making the development process more efficient.

5.Integrated Development Server: Flask comes with a built-in development server, making it convenient 
to develop and test applications locally without requiring a separate server setup.

6.Scalability: Flask allows for easy scalability as applications can be built modularly, and additional 
components can be added as needed. It can handle small to large-scale applications efficiently.

7.Pythonic: Flask follows the principles of Python, making it familiar and comfortable for Python
developers. It leverages the simplicity and elegance of Python in web development.
"""
# Create a simple Flask application to display 'Hello World!!'. Attach the screenshot of the output in Jupyter Notebook.
from flask import Flask

app = Flask(__name__)

@app.route("/hello_world")
def hello_world():
    return "<h1>'Hello, World!!'</h1>"

if __name__=="__main__":
    app.run(host="0.0.0.0")

#drive link of screenshot hello world : (https://drive.google.com/drive/folders/19EFsVr0Pkg8XDnSHYpYS34CKTJSWDdTo)

#Q3. What is App routing in Flask? Why do we use app routes?
""" 
App routing in Flask refers to the process of mapping URLs to specific functions or views in the 
application. It allows you to define different routes or endpoints that the application can handle.

In Flask, the @app.route() decorator is used to define routes. It associates a URL pattern with a Python 
function that will be executed when that URL is requested by the client.

We use app routes in Flask to define the different pages or resources that the application provides. 
Each route corresponds to a specific URL, and when a client makes a request to that URL, 
Flask invokes the associated function or view to generate a response.

App routes provide a way to organize the functionality of a web application, making it easy to handle 
different URLs and manage the flow of the application. It allows for building multi-page applications 
and handling different HTTP methods like GET, POST, etc., for each route.
"""
#Q4. Create a "/welcome" route to display the welcome message "Welcome to ABC Corporation" and a "/" route to show the following details:
#Company Name: ABC Corporation
#Location: India
#Contact Detail: 999-999-9999

from flask import Flask

app = Flask(__name__)

@app.route('/welcome')
def welcome():
    return "<h1>Welcome to ABC Corporation<h1>"

@app.route('/')
def company_details():
    return """Company Name: ABC Corporation
Location: India
Contact Detail: 999-999-9999"""

if __name__ == '__main__':
    app.run()

#Q5. What function is used in Flask for URL Building? Write a Python code to demonstrate the working of the url_for() function.
""" 
In Flask, the url_for() function is used for URL building. 
It generates a URL for the specified endpoint (view function) by taking into account the routing rules defined in the application.
"""
from flask import Flask, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return 'Home Page'

@app.route('/about')
def about():
    return 'About Page'

@app.route('/user/<username>')
def profile(username):
    return f'Profile Page of {username}'

if __name__ == '__main__':
    with app.test_request_context():
        print(url_for('home'))  
        print(url_for('about'))  
        print(url_for('profile', username='John')) 







