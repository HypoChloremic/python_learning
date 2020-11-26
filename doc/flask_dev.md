# Flask Development

#### HTTP methods

Assume we start with

```python
from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello():
    return 'hello'
```

the `route` decorator by default (aka default argument, arg, for the method) is to respond to solely `GET` requests. If we wish to also include `POST` requests:

```python
from flask import request
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        show_the_login_form()
```

So what we note from the code is that to interact with the `HTTP.request` we `from flask import request`, using the `request` class. 

#### Static files

Dynamic web apps also need static files: usually where the CSS and JS files are. 

Ideally, the webserver is configured to serve them. But during development, Flask can also do it. 

Create the folder `/static` in the package, or next to module, and it will be available at `/static` on the app.

To generate URLs for static files, we use the `static` endpoint name:

```python
url_for('static', filename='style.css')
```

This file is stored at: `static/style.css`

