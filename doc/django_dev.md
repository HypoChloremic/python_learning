# Django development
### Versions
Currently: env webdev, python 3.9.1, django 3.1.4
## Starting a project - Tut


To start a project, `cd` into the relevant directory, where the project folder is going to be located:
Run subsequently

```bash
>>> django-admin startproject proj1
```

### Where to store the code 
in `PHP`, code is stored under the web servers root: `/var/www`.
This is not done in django. None of the python code should  be within the web server's root, because people may be able to view the code. 
The documentation states to place the code somewehere else, such as `/home/mycode`... however, it is unclear if this falls in the project folder?

### Contens of the genereated project
```
mysite/
    manage.py
    mysite/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
```
These files are:

* The outer mysite/ root directory is a container for your project. Its name doesn’t matter to Django; you can rename it to anything you like.

* manage.py: A command-line utility that lets you interact with this Django project in various ways. You can read all the details about manage.py in django-admin and manage.py.

* The inner mysite/ directory is the actual Python package for your project. Its name is the Python package name you’ll need to use to import anything inside it (e.g. mysite.urls).

* mysite/__init__.py: An empty file that tells Python that this directory should be considered a Python package. If you’re a Python beginner, read more about packages in the official Python docs.

* mysite/settings.py: Settings/configuration for this Django project. Django settings will tell you all about how settings work.

* mysite/urls.py: The URL declarations for this Django project; a “table of contents” of your Django-powered site. You can read more about URLs in URL dispatcher.

* mysite/asgi.py: An entry-point for ASGI-compatible web servers to serve your project. See How to deploy with ASGI for more details.

* mysite/wsgi.py: An entry-point for WSGI-compatible web servers to serve your project. See How to deploy with WSGI for more details

### Test run the generated project
`cd` to the directory where `manage.py` is located. Run the file with python, passing the `runserver` as an argument:

```bash
>>> python manage.py runserver
```

### Migrations
Seemingly there may be the following warning message:

```bash
You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
```

### Minor note on the light-weight server and apache
Django ships with a light-weight server option, relieving us from the need of implementing it in `Apache`. instead we can wait until production time before shipping it with apache. 


### Changing port and IP


Changing the port

By default, the runserver command starts the development server on the internal IP at port 8000.

If you want to change the server’s port, pass it as a command-line argument. For instance, this command starts the server on port 8080:


$ python manage.py runserver 8080

If you want to change the server’s IP, pass it along with the port. For example, to listen on all available public IPs (which is useful if you are running Vagrant or want to show off your work on other computers on the network), use:


$ python manage.py runserver 0:8000

0 is a shortcut for 0.0.0.0. Full docs for the development server can be found in the runserver reference.

### Restarting the server and refreshing code

***Note***: The development server automatically reloads Python code for each request as needed. You don’t need to restart the server for code changes to take effect. However, some actions like adding files don’t trigger a restart, so you’ll have to restart the server in these cases.

### Projects vs apps

What’s the difference between a project and an app? An app is a Web application that does something – e.g., a Weblog system, a database of public records or a small poll app. A project is a collection of configuration and apps for a particular website. A project can contain multiple apps. An app can be in multiple projects.

### apps location
apps can live anywhere in the `Python path` (i.e. the path that is searched for when running `>>> python` in the terminal). 

### Create an app
In the same directory as `manage.py`, run `python manage.py startapp polls`, which generates

```bash
polls/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    views.py
```

This directory structure will house the poll application.

## The Polls App - tut
### Writing first view
open `polls/views.py`. Insert:

```python
from django.http import HttpRequest

def index(requst):
    return HttpResponse("hello world...")
```

This is the simplest view possible in Django. To call the view, we need to map it to a URL - and for this we need a URLconf.

To create a URLconf in the polls directory, create a file called urls.py. Your app directory should now look like:

```
polls/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    urls.py
    views.py
```

In the `polls/urls.py` include the following code. 
```python
from django-urls import paths
from . import views # accessing the `views.py` file that we modded above, and the `index` method

urlpatterns = [
    path("", views.index, name="index")
]
```
The next step is to point the root URLconf at the polls.urls module. When referring to the ***root*** URLconf, we are referring to `mysite`! 
In mysite/urls.py, add an import for django.urls.include and insert an include() in the urlpatterns list, so you have: 

`mysite/urls.py`
```python
from django.contrib import admin # unclear what admin does
from django.urls import include, path

urlpatterns = [
    path("polls/", include("polls.urls")), # this may be referring to the `urls.py` file in `polls` folder...
    path("admin/", admin.site.urls),
]
```
The `include()` function allows referencing other URLconfs. 

Whenever Django encounters `include()`, it ***chops off whatever part of the URL matched up to that point and sends the remaining string to the included URLconf for further processing***.

Alltså, om vi då har i `mysite/mysite/urls.py` följande:
```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
]
```
sen följande i `mysite/polls/urls.py`
```python
from django.urls import path
from . import views

urlpatterns = [
    path("pp", views.index, name="index"),
]
```
Då när vi access: `http://127.0.0.1:8000/polls/pp` kommer vi få svaret. Notera `pp` i slutet, som vi adderade i den `include()` pathen! Alltså moddade vi the `urlpatterns`

The idea behind `include()` is to make it easy to plug-and-play URLs. Since polls are in their own URLconf (polls/urls.py), 
they can be placed under “/polls/”, or under “/fun_polls/”, or under “/content/polls/”, or any other path root, and the app will still work.

### when to use include()

You should always use `include()` when you include other URL patterns. `admin.site.urls` is the only exception to this.

### verify the index view
You have now wired an index view into the URLconf. Verify it’s working with `...\> py manage.py runserver`


# Some details

## path()
The `path()` returns an element, which in turn is put inside the 
`list` object `urlpatterns`

Parameters: `path(route, view, kwargs=None, name=None)`
* the `route` argument = the url pattern. can contain angle brackets e.g. `<str:username>` to capture that part of the url and send it as a keyword *to* `view`.
    * Note that inside the angled brackets, it is possible to use typcasting, limiting the content type of that part of the url, e.g. `<int:section>` etc. 
* the `view` argument is a "view function", which is a result of `as_view()`. This is for class-based views


## include()
The `include()` the following can be read in the docs "Takes a full import path to another URLconf module that should be “included” in this place."

example:
```python
path(route='index', view=include('polls.urls'))
```

what `include('polls.urls')` will then do is to go into the import path of `polls.urls` and then 

## django views
`views` in django is key for *apps*, built in django. Simplified take: 
* a function/class takes a ***web request*** and returns a ***web response***

### Capabilities of views
***Views can***:
* fetch objects from database, 
* modify those objects, 
* render forms, 
* return HTML, 
* and more. 

***Note***: 
* from django "a view function, `view` for short, is a function that takes ***Web request*** and ***returns*** a ***Web response***. This response can be the HTML contents of a Web page, or a redirect, or a 404 error, or an XML document, or an image . . . or anything, really."
* The view itself contains whatever arbitrary logic is necessary to return that response.

### Two types of views
there is the `function-based views (FBVs)`, and `class-based views (CBVs)`. CBVs was added after FBVs, it adds modularity and functionality, so we dont have to rewrite code over and over. 

Django ships with a bunch of different CBVs that we can use. 

An example of a view that returns a current date and time, as HTML:
```python
from django.http import HttpResponse
import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)
```

So this script can be stored anywhere on the Python path, ***Implying that it should be somewhere where we can use `import`** 