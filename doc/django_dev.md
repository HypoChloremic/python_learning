# Django Beginner Project
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

## Database setup
Open `mysite/settings.py`. its a normal `module` (that can be imported yani), with module-level variables representing django settings.

### By default
By default, it is configred to use SQLite, which is the easiest choice. SQLite is included in python, no need to install anything. 

### Changing database
instead of the default database, it is possible to use different ones. 

to do this, install the appropriate `database bindings` and change the following keys in the `mysite/settings.py` file: `DATABASES` `'default'` item and match your database connection settings: 
* `ENGINE`: either `django.db.backends.sqlite3`, `django.db.backends.postgresql`, `django.db.backends.mysql`, or `django.db.backends.oracle`. More are also available
* `NAME`: the name of your database. if `SQLite`, the databse will be a file on our computer. in this case, `NAME` should be the full absoltue path, including filename, of that file. 
    * the default `BASE_DIR / 'db.sqlite3'` will store the file in our project directory. 

###  For databases other than SQLite

If you’re using a database besides SQLite, make sure you’ve created a database by this point. Do that with “CREATE DATABASE database_name;” within your database’s interactive prompt.

Also make sure that the database user provided in mysite/settings.py has “create database” privileges. This allows automatic creation of a test database which will be needed in a later tutorial.

If you’re using SQLite, you don’t need to create anything beforehand - the database file will be created automatically when it is needed.


#### In not SQLite
if you are not using SQLite as your database, additional settings such as USER, PASSWORD, and HOST must be added. For more details, see the reference documentation for DATABASES.


### INSTALLED APPS
Also, note in `mytesite/settings.py` the `INSTALLED_APPS` setting at the top of the file. That holds the names of all Django applications that are activated in this Django instance. Apps can be used in multiple projects, and you can package and distribute them for use by others in their projects.

* `django.contrib.admin` – The admin site. You’ll use it shortly.
* `django.contrib.auth` – An authentication system.
* `django.contrib.contenttypes` – A framework for content types.
* `django.contrib.sessions` – A session framework.
* `django.contrib.messages` – A messaging framework.
* `django.contrib.staticfiles` – A framework for managing static files.

#### Database tables
Some of these installed apps use at least one `database table`. So we need to create the tables in the database, before we can use them. 

To build the `database tables`:

```bash
>>> python manage.py migrate
```
#### migrate command
the `migrate` command through `manage.py`, looks at `INSTALLED_APPS` settinsg and creates any necessary datbase tables, in accord to the databse settings in `mysite/settings.py`

##### Running command-line database client
To start the command-line database client, in the terminal/cmd run `sqlite3`. Note that the command will depend on the databse that we are runnnig and the client that the database ships with, so it may be different than `sqlite3`.  

NOTE: `SQL` has line-terminators with `;`, in order to run the code. 

If you’re interested, run the command-line client for your database and type \dt (PostgreSQL), SHOW TABLES; (MariaDB, MySQL), .schema (SQLite), or SELECT TABLE_NAME FROM USER_TABLES; (Oracle) to display the tables Django created.

We ran SQLite. 

### Creating models
Now we will define our models, the database layout with more metadata. 

#### What a model is
* The model = single definitive source of truth *about* our data 
* It contains the essential dields and behaviors of the data your storing. 
* ***DRY principle*** is being used
* goal = to define our data model in one place, and automatically *derive* things from it. 
* Includes migrations, unlike Ruby on rails, migrations are entirely derived from the our models file. and are essentially a hitory that django can roll thry to update our databse schema to match our current models.

#### In our poll app
we wish to create two models: Question and a choice. 
* Question has question and publication data
* choice has two fields, the text of the choice, and the vote tally. 
* each choice is associated with a question

These concept are represented by Python classes.

edit `polls/models.py`:

```python
from django.db import models

class Question(models.Model):
    question_text = models.Charfield(max_length=200)
    pub_date = models.DateTimeField("Date published")

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
```

* Each model here (Question and Choice) are rerpesenterd by a class that *subclasses* `django.db.models.Model`. 
* There are a number of class variables in each model (e.g. `question_text`), which represent ***database field in the model***. 
* Each field represented by *an instance* to a `Field` class. e.g. `CharField` and `IntegerField`. This tells django what type of data is contained in each field. 
* the `field names`, e.g. `question_text` will be is the names we will use when we refer to the fields, and will be the `columns` in the database. 
* Finally, note a relationship is defined, using ForeignKey. That tells Django each Choice is related to a single Question. Django supports all the common database relationships: many-to-one, many-to-many, and one-to-one

#### Activating models
Small bit of code in models, gives Django a lot of info. With it, django will:
* create a databse schema (`CREATE TABLE` statements) for the app
* create a Python databse-access API för accessing `Question` and `Choice` objects. 

### Install our Polls app
Because apps in django can be used in multiple projects, we need to tell our current project to install the app we have created. 
* Add a reference to the `polls` configuration class, in the `INSTALLED_APPS` setting. 
* `PollsConfig` class is located in the `polls/apps.py`
    * the path is therefore `polls.apps.PollsConfig`

edit `mysite/settings.py` and add the dotted path (dotted path = the import path) to `INSTALLED_APPS` setting. 

```python
INSTALLED_APPS = [
    'polls.apps.PollsConfig', # this was added
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

Django now *knows* to run *include* polls app. Run the following;

```bash
> python manage.py makemaigrations polls

Migrations for 'polls':
  polls/migrations/0001_initial.py
    - Create model Question
    - Create model Choice
```
##### makemigrations
`makemigrations` tells django that we have made changes to our models or made new ones in our case, to be 'stored as migrations'

* "migrations" are how django stores changs to models, thus databse schema.
* They are files on the disk. 

##### Read the migrations
we can read the migrations: `polls/migrations/0001_initial.py`

##### Read the sql generated
There’s a command that will run the migrations for you and manage your database schema automatically - that’s called migrate, and we’ll come to it in a moment - but first, let’s see what SQL that migration would run. The sqlmigrate command takes migration names and returns their SQL:

```bash
>>>>>> python migrate.py sqlmigrate polls 0001

BEGIN;
--
-- Create model Question
--
CREATE TABLE "polls_question" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "question_text" varchar(200) NOT NULL, "pub_date" datetime NOT NULL);
--
-- Create model Choice
--
CREATE TABLE "polls_choice" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "choice_text" varchar(200) NOT NULL, "votes" integer NOT NULL, "question_id" integer NOT NULL REFERENCES "polls_question" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE INDEX "polls_choice_question_id_c5b4b260" ON "polls_choice" ("question_id");
COMMIT;
```

* Table names are automatically generated by combining the name of the app (polls)and the lowercase name of the model – question and choice. (You can override this behavior.)
* Primary keys (IDs) are added automatically. (You can override this, too.)
* By convention, Django appends "_id" to the foreign key field name. (Yes, you can override this, as well.)
* The foreign key relationship is made explicit by a FOREIGN KEY constraint. Don’t worry about the DEFERRABLE parts; it’s telling PostgreSQL to not enforce the foreign key until the end of the transaction.
* It’s tailored to the database you’re using, so database-specific field types such as auto_increment (MySQL), serial (PostgreSQL), or integer primary key autoincrement (SQLite) are handled for you automatically. Same goes for the quoting of field names – e.g., using double quotes or single quotes.
* The sqlmigrate ***command doesn’t actually run the migration*** on your database - instead, it prints it to the screen so that you can see what SQL Django thinks is required. It’s useful for checking what Django is going to do or if you have database administrators who require SQL scripts for changes.

##### check for problems migrations
If you’re interested, you can also run python manage.py check; this checks for any problems in your project without making migrations or touching the database.

#### Run migrate again
Now, run migrate again to create those model tables in your database:

```bash
>>> python manage.py migrate

Operations to perform:
  Apply all migrations: admin, auth, contenttypes, polls, sessions
Running migrations:
  Applying polls.0001_initial... OK
```


#### Three-step guide for models changes
1. Chnage your models in `models.py`
2. run `python manage.py makemigrations` to create migrations for those changes
3. run `python manage.py migrate` to apply those changes to the database

## Playing with the database API

There is an interactive django API we can use. To invoke the shell use: 

To invoke the shell: 
`>>> python manage.py shell`

We are doing this, instead of simply tuping `python`. `manage.py` sets the `DJANGO_SETTINGS_MODULE` env variable, giving Django the python import path to `mysite/settings.py`. 

#### Exploring the database API
Once in the shell, we explore `database API`
```python
>>> from polls.models import Choice, Question  # Import the model classes we just wrote.

# No questions are in the system yet.
>>> Question.objects.all()
<QuerySet []>

# Create a new Question.
# Support for time zones is enabled in the default settings file, so
# Django expects a datetime with tzinfo for pub_date. Use timezone.now()
# instead of datetime.datetime.now() and it will do the right thing.
>>> from django.utils import timezone
>>> q = Question(question_text="What's new?", pub_date=timezone.now())

# Save the object into the database. You have to call save() explicitly.
>>> q.save()

# Now it has an ID.
>>> q.id
1

# Access model field values via Python attributes.
>>> q.question_text
"What's new?"
>>> q.pub_date
datetime.datetime(2012, 2, 26, 13, 0, 0, 775217, tzinfo=<UTC>)

# Change values by changing the attributes, then calling save().
>>> q.question_text = "What's up?"
>>> q.save()

# objects.all() displays all the questions in the database.
>>> Question.objects.all()
<QuerySet [<Question: Question object (1)>]>
```

Wait a minute. `<Question: Question object (1)>` isn’t a helpful representation of this object. Let’s fix that by editing the Question model (in the polls/models.py file) and adding a __str__() method to both Question and Choice:

##### adding __str__()
So this is nice, that we do not like the direct representation when we write `polls.models.Question` in the shell, that we wish to modify the output: 

in `polls/models.py`

```python
from django.db import models

class Question(models.Model):
    ...

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    ...

    def __str__(self):
        return self.choice_text
```
I.e. we wish when we call the `polls.models.Choice` or `Question` objects, that the fields we have input will be returned

It’s important to add __str__() methods to your models, not only for your own convenience when dealing with the interactive prompt, but also because objects’ representations are used throughout Django’s automatically-generated admin.

##### adding custom method to model
in `polls/models.py`

```python
import datetime
from django.db import models
from django.utils import timezone

class Question(models.Model):
    # ...
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
```

Save these changes (we do not need to run `python manage.py migrate`, just save the code to the file) and start a new Python interactive shell by running `python manage.py shell` again:
```python
>>> from polls.models import Choice, Question

# Make sure our __str__() addition worked.
>>> Question.objects.all()
<QuerySet [<Question: What's up?>]>

# Django provides a rich database lookup API that's entirely driven by
# keyword arguments.
>>> Question.objects.filter(id=1)
<QuerySet [<Question: What's up?>]>
           
>>> Question.objects.filter(question_text__startswith='What')
<QuerySet [<Question: What's up?>]>

# Get the question that was published this year.
>>> from django.utils import timezone
>>> current_year = timezone.now().year
>>> Question.objects.get(pub_date__year=current_year)
<Question: What's up?>

# Request an ID that doesn't exist, this will raise an exception.
>>> Question.objects.get(id=2)
Traceback (most recent call last):
    ...
DoesNotExist: Question matching query does not exist.

# Lookup by a primary key is the most common case, so Django provides a
# shortcut for primary-key exact lookups.
# The following is identical to Question.objects.get(id=1).
>>> Question.objects.get(pk=1)
<Question: What's up?>

# Make sure our custom method worked.
>>> q = Question.objects.get(pk=1)
>>> q.was_published_recently()
True
```

```python
# Give the Question a couple of Choices. The create call constructs a new
# Choice object, does the INSERT statement, adds the choice to the set
# of available choices and returns the new Choice object. Django creates
# a set to hold the "other side" of a ForeignKey relation
# (e.g. a question's choice) which can be accessed via the API.
>>> q = Question.objects.get(pk=1)

# Display any choices from the related object set -- none so far.
>>> q.choice_set.all()
<QuerySet []>

# Create three choices.
>>> q.choice_set.create(choice_text='Not much', votes=0)
<Choice: Not much>
>>> q.choice_set.create(choice_text='The sky', votes=0)
<Choice: The sky>
>>> c = q.choice_set.create(choice_text='Just hacking again', votes=0)

# Choice objects have API access to their related Question objects.
>>> c.question
<Question: What's up?>

# And vice versa: Question objects get access to Choice objects.
>>> q.choice_set.all()
<QuerySet [<Choice: Not much>, <Choice: The sky>, <Choice: Just hacking again>]>
>>> q.choice_set.count()
3
```

###### Deleting one of the choices
```python
# The API automatically follows relationships as far as you need.
# Use double underscores to separate relationships.
# This works as many levels deep as you want; there's no limit.
# Find all Choices for any question whose pub_date is in this year
# (reusing the 'current_year' variable we created above).
>>> Choice.objects.filter(question__pub_date__year=current_year)
<QuerySet [<Choice: Not much>, <Choice: The sky>, <Choice: Just hacking again>]>

# Let's delete one of the choices. Use delete() for that.
>>> c = q.choice_set.filter(choice_text__startswith='Just hacking')
>>> c.delete()
```

###### General
Check down below why `choice_set` specifically is used, it related to the Django backtracing ORM, that automatically generates the fields when using `ForeignKey`. 

### The Django admin
Generating admin sites for your staff or clients to add, change, and delete content is tedious work that doesn’t require much creativity. For that reason, Django entirely automates creation of admin interfaces for models.

Django was written in a newsroom environment, with a very clear separation between “content publishers” and the “public” site. 

Site managers use the system to add news stories, events, sports scores, etc., and that content is displayed on the public site. 

Django solves the problem of creating a unified interface for site administrators to edit content.

The admin isn’t intended to be used by site visitors. It’s for site managers.

#### Creating an admin user

Need a user who can login to the admin site: Run the following:
```
>>> python manage.py createsuperuser
username: admin
email address: admin@example.com
Password: *******
Password (again): ******
Superuser created successfully
```

#### Start the (development) server
Let us run the server now:
`python manage.py runserver`

and go to the admin page `http://127.0.0.1:8000/admin/`
and sign in. 

#### Inside the admin page
We are presented by "editable content": `groups` and `users`. These are provided by `django.contrib.auth`

#### Make the poll app modifiable in the admin
The poll app is not displayed seemingly on the admin index page. 
we need to tell the admin that Question objects have an admin interface. To do this, open the `polls/admin.py` file, and edit it to look like this:

```python
from django.contrib import admin

from .models import Question

admin.site.register(Question)
```

Save it to file, and just reload the admin page, and we will se it on the admin index page! 

##### The Questions page

Enter the Questions page

The form is automatically generated from the Question model.
The different model field types (DateTimeField, CharField) correspond to the appropriate HTML input widget. Each type of field knows how to display itself in the Django admin.

Each DateTimeField gets free JavaScript shortcuts. Dates get a “Today” shortcut and calendar popup, and times get a “Now” shortcut and a convenient popup that lists commonly entered times.


### Views
* In Django, web pages and other content are delivered by views. Each view is represented by a Python function (or method, in the case of class-based views). 
* Django will choose a view by examining the URL that’s requested (to be precise, the part of the URL after the domain name)

#### URLconfs
A URL pattern is the general form of a URL - for example: /newsarchive/<year>/<month>/.

To get from a URL to a view, Django uses what are known as ‘URLconfs’. A URLconf maps URL patterns to views.

#### writing more views

`polls/views.py`

```python
def detail(request, qustion_id):
    return HttpResponse(f"You're looking at question {question_id}.")

def results(request, question_id):
    response = f"You're looking at the results of question {question_id}."
    return HttpResponse(response)

def vote(request, question_id):
    return HttpResponse(f"You're  voting on question {question_id}.")
```

Note that we are using the variable `question_id`

```python
from django.urls import path
from . import views

urlpatterns = [
    path("pp", views.index, name="index"),
    path("<int:question_id>/", views.detail, name="detail"),
    path("<int:question_id>/results/>", views.results, name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote")
]
```

om vi därför matar in `http://127.0.0.1:8000/polls/100/` så får vi `print`: 
"You're looking at question 100."

When somebody requests a page from your website – say, “/polls/34/”: 
* Django will load the mysite.urls Python module because it’s pointed to by the ROOT_URLCONF setting. 
* It finds the variable named urlpatterns and traverses the patterns in order. 
* After finding the match at 'polls/', it strips off the matching text ("polls/") and sends the remaining text – "34/" – to the ‘polls.urls’ URLconf for further processing. 
* There it matches '<int:question_id>/', resulting in a call to the detail() view like so: `detail(request=<HttpRequest object>, question_id=34)`

#### Writing views that do stuff
Each view is responsible for doing one of two things: returning an `HttpResponse` object containing the content for the requested page, or raising an exception such as `Http404`. The rest is up to you

Your view can read records from a database, or not. It can use a template system such as Django’s – or a third-party Python template system – or not. It can generate a PDF file, output XML, create a ZIP file on the fly, anything you want, using whatever Python libraries you want.

All Django wants is that `HttpResponse`. Or an exception.


Let’s use Django’s own database API, which we covered in Tutorial 2. Here’s one stab at a new `index()` view, which displays the latest 5 poll questions in the system, separated by commas, according to publication date:


`polls/views.py`
```python
from django.http import HttpResponse

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)

# Leave the rest of the views (detail, results, vote) unchanged
```
There’s a problem here, though: the page’s design is hard-coded in the view. If you want to change the way the page looks, you’ll have to edit this Python code. So let’s use Django’s template system to separate the design from Python by creating a template that the view can use.

In `$ python manage.py shell`, one can add more question objects:
```python
> from django.utils import timezone
> from polls.models import Question, Choice
>
> random_q = Question(question_text="random text", pub_date=timezone.now())
> random_q.save()
```

#### Templates - `polls/templates`

First, create a directory called templates in your polls directory. Django will look for templates in there.

Your project's `TEMPLATES` setting describe how Django will load and render templates. The default settings file configures a `DjangoTemplates` backend, whose `APP_DIRS` options is set to `True`. By convention, `DjangoTemplates` looks for a "templates" subdirectory in each of the `INSTALLED_APPS`.

In the `polls/templates` folder, create another folder called `polls`, within which an `index.html`. Thus `polls/templates/polls/index.html`. 

Due to how the `app_directories` template loader works, as described above... you can refer to this template within django as `polls/index.html`!


##### Template namespacing

Now we might be able to get away with putting our templates directly in polls/templates (rather than creating another polls subdirectory), but it would actually be a bad idea. Django will choose the first template it finds whose name matches, and if you had a template with the same name in a different application, Django would be unable to distinguish between them. We need to be able to point Django at the right one, and the best way to ensure this is by namespacing them. That is, by putting those templates inside another directory named for the application itself.


##### Creating template index.html
in `polls/templates/polls/index.html`
```python
{% if latest_question_list %}
    <ul>
        {% for question in latest_question_list %}
            <li>
                <a href="/polls/{{ question.id }}/">
                    {{ question.question_text }}
                </a>
            </li>
        {% endfor %}
        </ul>
{% else %}
        <p>No polls are available</p>
{% endif %}
```

##### Updating the index view with template
Now let’s update our index view in `polls/views.py` to use the template:
```python
from django.http import HttpResponse
from django.template import loader

from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]

    # This is the important part, as it will allow us
    # to bring in the template we created
    template = loader.get_template("polls/index.html")

    context = {
        "latest_question_list": latest_question_list,        
    }

    return HttpResponse(template.render(context, request))
```
Via `django.template.loader("polls/index.html")` we will be able to laod the template, and pass it a context. 

***The context is a dictionary which maps variable-names to Python objects***

Load the page by pointing yout browser at `/polls/`. 

#### A shortcut: render()

It’s common to load a template, fill a context and return an HttpResponse object with the rendered template. Django provides a shortcut. 

Here’s the full `index()` view, rewritten:
`polls/views.py`
```python
from django.shortcuts import render

from .models import Question'

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = { "latest_question_list": latest_question_list }
    return render(request, "polls/index.html", context)
```


Note that once we’ve done this in all these views, we no longer need to import loader and HttpResponse (you’ll want to keep `HttpResponse` if you still have the stub methods for `detail`, `result`, `vote`).


#### Raising a 404 error

Now, lets tackle the "question detail view". The page that displays the qeston text for a given poll. 

Here's the view
`polls/views.py`

```python
from django.http import Http404
from django.shortcuts import render

from .models import Question

# ... all the rest

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        # This is where the 404 error occurs, it will exist the 
        # method
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})
```

We’ll discuss what you could put in that polls/detail.html template a bit later, but if you’d like to quickly get the above example working, a file containing just:

`polls/templates/polls/detail.html`
```html
{{ question }}
```


#### Shortcut for get_object_or_404()
It's very common to use `get()` and raise `Http404`, if the object doesnt exist. Django provides a shortcut. here's detail view, rewritten:

`polls/views.py`

```python
from django.shortcuts import get_object_or_404, render

from .models import Question

# [...]

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {"question": question}
    return render(request, "polls/detail.html", context)
```

The get_object_or_404() function takes a Django model as its first argument and an arbitrary number of keyword arguments, which it passes to the `get()` function of the ***model’s manager*** (i.e. the `Question` class model we). It raises Http404 if the object doesn’t exist.

There’s also a get_list_or_404() function, which works just as get_object_or_404() – except using filter() instead of get(). It raises Http404 if the list is empty.


### Use the Template System
Back to the `detail()` view for our poll application. Given the `context` variable `question`, here's what the `polls/detail.html` could look like:

`polls/template/polls/detail.html`

```html
<h1>{{ question.question_text }}</h1>
<ul>
{% for choice in question.choice_set.all %}
    <li>{{ choice.choice_text }}</li>
{% endfor %}
</ul>
```
#### dot-lookup syntax in templates

The template system uses dot-lookup syntax to access variable attributes. In the example of `{{ question.question_text }}`, first Django does a dictionary lookup on the object `question`. Failing that, it tries an attribute lookup – which works, in this case. If attribute lookup had failed, it would’ve tried a list-index lookup.

#### Method calling in templates
***Method-calling*** happens in the `{% for %} loop: question.choice_set.all` is interpreted as the `question.choice_set.all()` (in Python code ya3ni, note the `all()` method), which returns an iterable of `Choice` objects and is suitable for use in the `{% for %}` tag.

See the https://docs.djangoproject.com/en/3.1/topics/templates/ guide for more about templates.


### Removing harcode URLs in templates
Recall when we reote the link to a `question` in `polls/index.html`, the link was harcoded as:
`<li><a href="/polls/{{ question.id }}/">{{question.question_text}}</a></li>`

The problem with this hardcoded, tightly-coupled approach is that it becomes challenging to change URLs on projects with a lot of templates. 

However, since you defined the `name` argument in the `path()` functions in the `polls.urls` module, you can ***remove a reliance on specific URL paths*** defined in your url configurations by using the `{% url %}` template tag:

`<li><a href="{% url 'detail' question.id %}">{{ question.question_text }}</a></li>`


The way this works is by looking up the URL definition as specified in the polls.urls module. 

You can see exactly where the URL name of ‘detail’ is defined below:
```python
# ...
# the 'name' value as called by the {% url %} template tag
path('<int:question_id>/', views.detail, name='detail'),
# ...
```

### Namespacing URL names

The tutorial project has just one app, polls. In real Django projects, there might be five, ten, twenty apps or more. How does Django differentiate the URL names between them? For example, the polls app has a `detail` view, and so might an app on the same project that is for a blog. How does one make it so that Django knows which app view to create for a url when using the `{% url %}` template tag?

The answer is to add `namespaces` to your URLconf. In the `polls/urls.py` file, go ahead and add an `app_name` to set the application namespace:

`polls/urls.py`

```python
from django.urls import path

from . import views

app_name = 'polls' # this is the new part
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
```

Now change your `polls/index.html` template from:
```html
<li><a href="{% url 'detail' question.id %}">{{ question.question_text }}</a></li>
```

into 

`polls/templates/polls/index.html`

```html
<li><a href="{% url 'polls:detail' question.id %}">{{ question.question_text }}</a></li>
```

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

So this script can be stored anywhere on the Python path, ***Implying that it should be somewhere where we can use `import`*** 

## models.ForeignKey
In the tutorial, we write in the `Choice` class the following:
`question = models.ForeignKey(Question, on_delete = models.CASCADE)`

Thus, each `Choice` has explicitly a `Question` field, which we declared in the model. 

### The django ORM object-relational mapping layer 
Django's ORM, follows the relationship between `Choice` and therefore `Question` backwards!

It will ***automatically*** generate a field ***on each instance (of `Question`?)*** called `foo_set`, where `foo` is the model (i.e. `Choice`) with a `ForeignKey` field ***to that*** model (i.e. `Question`).

* Therefore, `choice_set` becomes a field available to the `Question` object. 
* `choice_set` is a `RelatedManager`, which isa ble to create querysets of `Choice` objects, which ***relate*** to the `Question` instance, e.g. `q.choice_set.all()`

### Parameters
* `related_name`: for the example above, django automatically generates `foo_set -> choice_set`, but we can manuallt set the name. for instance `ForeignKey(related_name="Choice_set")`

## class RelatedManager
In the standard tutorial, as we write about the `ForeignKey` part, is that `choice_set` becomes a `RelatedManager`. This manager in turn ships with a bunch of methods

https://docs.djangoproject.com/en/3.1/ref/models/relations/

the create method is mentioned there. 

### RelatedManger.create()
Seemingly this will generate a ***NEW*** object `Choice`, then attaching it to the `Question` object. 

### RelatedManager.all()
```python
>>> q.Choice_set.all()
<QuerySet [<Choice: Not much>, <Choice: The sky>, <Choice: Just hacking again>]>
```