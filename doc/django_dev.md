# Django development
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


```