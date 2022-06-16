# AirBnB_clone
This first step consists of a custom command-line interface for data management, and the base classes for the storage of this data.

## Description
This team project is part of the ALX School Full-Stack Software Engineer program. 
It's the first step towards building a first full web application: an AirBnB clone. This first step consists of a custom command-line interface for data management, and the base classes for the storage of this data.

Resources
Read or watch:
* [cmd module](https://docs.python.org/3.4/library/cmd.html)
* packages concept page
* [uuid module](https://docs.python.org/3.4/library/uuid.html)
* [datetime](https://docs.python.org/3.4/library/datetime.html)
* [unittest module](https://docs.python.org/3.4/library/unittest.html#module-unittest)
* [args/kwargs](https://yasoob.me/2013/08/04/args-and-kwargs-in-python-explained/)
* [Python test cheatsheet](https://www.pythonsheets.com/notes/python-tests.html)

# Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

# General
* How to create a Python package
* How to create a command interpreter in Python using the cmd module
* What is Unit testing and how to implement it in a large project
* How to serialize and deserialize a Class
* How to write and read a JSON file
* How to manage datetime
* What is an UUID
* What is *args and how to use it
* What is **kwargs and how to use it
* How to handle named arguments in a function


# Requirements
## Python Scripts
* Allowed editors: ``vi, vim, emacs``
* All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
* All your files should end with a new line
* The first line of all your files should be exactly #!/usr/bin/python3
* A README.md file, at the root of the folder of the project, is mandatory
* Your code should use the pycodestyle (version 2.7.*)
* All your files must be executable
* The length of your files will be tested using ``wc``
* All your modules should have a documentation ``(python3 -c 'print(__import__("my_module").__doc__)')``
* All your classes should have a documentation ``(python3 -c 'print(__import__("my_module").MyClass.__doc__)')``
* All your functions (inside and outside a class) should have a documentation ``(python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c ```'print(__import__("my_module").MyClass.my_function.__doc__)')``
* A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

## Python Unit Tests
* Allowed editors: ``vi, vim, emacs``
* All your files should end with a new line
* All your test files should be inside a folder tests
* You have to use the [unittest module](https://docs.python.org/3.4/library/unittest.html#module-unittest)
* All your test files should be python files (extension: .py)
* All your test files and folders should start by ``test_``
* Your file organization in the tests folder should be the same as your project
* e.g., For models/base_model.py, unit tests must be in: ``tests/test_models/test_base_model.py``
* e.g., For models/user.py, unit tests must be in: ``tests/test_models/test_user.py``
* All your tests should be executed by using this command: ``python3 -m unittest discover tests``
* You can also test file by file by using this command: ``python3 -m unittest tests/test_models/test_base_model.py``
* All your modules should have a documentation ``(python3 -c 'print(__import__("my_module").__doc__)')``
* All your classes should have a documentation ``(python3 -c 'print(__import__("my_module").MyClass.__doc__)')``
* All your functions (inside and outside a class) should have a documentation ``(python3 -c 'print(__import__("my_module").my_function.__doc__)'`` and ``python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')``
* We strongly encourage you to work together on test cases, so that you don’t miss any edge case

## Execution
Your shell should work like this in interactive mode:
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```
But also in non-interactive mode: (like the Shell project in C)
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```

## Steps
You won’t build this application all at once, but step by step.

Each step will link to a concept:

## The console
* create your data model
* manage (create, update, destroy, etc) objects via a console / command interpreter
* store and persist objects to a file (JSON file)

The first piece is to manipulate a powerful storage system. This storage engine will give us an abstraction between “My object” and “How they are stored and persisted”. This means: from your console code (the command interpreter itself) and from the front-end and RestAPI you will build later, you won’t have to pay attention (take care) of how your objects are stored.

This abstraction will also allow you to change the type of storage easily without updating all of your codebase.

The console will be a tool to validate this storage engine.

## Files and Directories
* ``models`` directory will contain all classes used for the entire project. A class, called “model” in a OOP project is the representation of an object/instance.
* ``tests`` directory will contain all unit tests.
* ``console.py`` file is the entry point of our command interpreter.
* ``models/base_model.py`` file is the base class of all our models. It contains common elements:
  * attributes: ``id``, ``created_at`` and ``updated_at``
  * methods: ``save()`` and ``to_json()``
* ``models/engine`` directory will contain all storage classes (using the same prototype). For the moment you will have only one: ``file_storage.py``.

## Console and Command Usage

The console is a Unix shell-like command line user interface provided by the python [CmdModule](https://wiki.python.org/moin/CmdModule)
It prints a prompt and waits for the user for input, for our project we used **(hbnb)** 

Command | Example
------- | -------
Display commands help | ```(hbnb) help <command>```
Create object (prints its id)| ```(hbnb) create <class>```
Destroy object | ```(hbnb) destroy <class> <id>``` or ```(hbnb) <class>.destroy(<id>)```
Show object | ```(hbnb) show <class> <id>``` or ```(hbnb) <class>.show(<id>)```
Show "all" objects or instances class | ```(hbnb) all``` or ```(hbnb) all <class>```
Run console | ```./console.py```
Quit console | ```(hbnb) quit```


Help command example

```bash
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update
```

## Tests
All the code is tested with the **unittest** module.
The test for the classes are in the [test_models](./tests/test_models/) folder.

## Web static
* learn HTML/CSS
* create the HTML of your application
* create template of each object

## MySQL storage
* replace the file storage by a Database storage
* map your models to a table in database by using an O.R.M.

## Web framework - templating
* create your first web server in Python
* make your static HTML file dynamic by using objects stored in a file or database

## RESTful API
* expose all your objects stored via a JSON web interface
* manipulate your objects via a RESTful API

## Web dynamic
* learn JQuery
* load objects from the client side by using your own RESTful API

## Authors

* **Bernardine BAZUBAGIRA**
* [**Jackson Eyamu**](https://github.com/de-jackson)
