#Q1. Explain GET and POST methods.
""" 
GET: The GET method is used to request data from a specified resource. 
It is one of the HTTP methods used in web communication. When a client sends a GET request, 
it retrieves data from the server without modifying or changing any existing resources. 
The parameters or data are appended to the URL as query parameters. 
For example, when you enter a URL in your browser's address bar and press Enter, 
it typically sends a GET request to retrieve the web page.
"""
"""
POST: The POST method is used to submit data to be processed to a specified resource. 
It is also an HTTP method and is commonly used for submitting form data, uploading files, 
or performing actions that result in data modification or creation on the server. 
Unlike the GET method, the data sent with a POST request is included in the body 
of the request instead of being appended to the URL.
"""
#Q2. Why is request used in Flask?
"""
In Flask, the request object is used to access incoming request data such as form data, query parameters, headers,
and files. It provides a way to extract data from the HTTP request made by the client. 
The request object allows you to access and work with the data sent by the client, making it possible to handle
user input, process form submissions, and interact with the request headers. 
"""
#Q3. Why is redirect() used in Flask?
"""
In Flask, the redirect() function is used to perform a redirect to a different URL or route. 
It is a convenient way to redirect the user's browser to another page or route within the application. 
Redirects are commonly used after a successful form submission or to direct the user to a different 
part of the application based on certain conditions or actions. 
By using redirect(), you can easily control the flow of the user's navigation within your Flask application.
"""
#Q4. What are templates in Flask? Why is the render_template() function used?
""" 
Templates in Flask are files that contain the structure and layout of HTML pages with placeholders for dynamic content. 
They are typically written in HTML with added template-specific syntax. Templates separate the presentation logic 
from the business logic, making it easier to maintain and update the user interface of the application.
"""
"""
The render_template() function in Flask is used to render these templates and generate HTML responses dynamically. 
It takes the name of the template file as an argument and optionally accepts additional data to pass to the template.
The render_template() function processes the template, replaces placeholders with actual values, and returns the resulting HTML. 
By using templates and the render_template() function, you can create dynamic web pages in Flask that can incorporate 
data from the application and provide a customized user experience.
"""
#Q5. Create a simple API. Use Postman to test it. Attach the screenshot of the output in the Jupyter Notebook.

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api', methods=['POST'])
def api():
    data = request.json  
    message = f"Hello, {data['name']}!"
    response = {'message': message}
    return jsonify(response)

if __name__ == '__main__':
    app.run()
