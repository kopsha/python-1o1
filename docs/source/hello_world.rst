hello world
===========

A way to show the world that we are civil.

Python is a clean and powerful programming language. You can use it to build websites, analyze data, create nice graphs or simply automate those boring repetitive tasks.

*todo: how about some screenshots ?*

It has become a programmer tradition that when you learn a new programming language, you start with a program that only says "hello".


the console
^^^^^^^^^^^

First we need to verify if python is installed on our computer by opening the terminal application (for Windows users, type Win+R and then `cmd`).

Type in `python` and see what happens
    
.. code-block:: console

    macbook$ python
    Python 3.7.2 (default, Dec 27 2018, 07:35:52) 
    [Clang 10.0.0 (clang-1000.11.45.5)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>> _

If you see a version number and a prompt, you're good to go. But if you see an error, you need to download and install python. I recommend to visit the `python comunity website <http://www.python.org/>`_ and download the latest python3 version.

Let's get more familiar with the python console. The easiest way you can interact with the python interpreter is through this console. Here you can *talk* directly to the core python and send your request.
For example:

.. code-block:: console
    :caption: why don't you try some numbers or an expression, or some text, be creative

    Python 3.7.2 (default, Dec 27 2018, 07:35:52) 
    [Clang 10.0.0 (clang-1000.11.45.5)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>> 
    >>> 10 
    10
    >>> 10 + 10
    20
    >>> 10 + 2 * 3  
    16
    >>> 'hello'
    'hello'
    >>> 1/2
    0.5
    >>> 1 + 2)
      File "<stdin>", line 1
        1 + 2)
             ^
    SyntaxError: invalid syntax
    >>> _

Observe that python tries to *understand* what we type, be it numbers, arithmetic operations or strings, computes the result and prints it back for us. However, if we accidentally type something that doesn't make sense, *python* will do its best to point out the problem, but it will let us decide how and when we'll fix it.


saying hello
^^^^^^^^^^^^

Open the python console and type ``print("Hello world!")`` then enter:

.. code-block:: console
    :caption: et voilà

    >>> print("Hello world!")
    Hello world!
    >>> print(12)
    12
    >>> print(1 / 2)
    0
    >>> print(2 * 2)
    4
    >>> _

Notice that print behaves the same as the interpreter, it looks at our expression, tries to understand it and then prints the result


Now we'll say ``hello`` using a python program instead of the python interactive console, so exit python by typing ``quit()``

.. code-block:: console

    >>> quit()
    macbook$ _


Create a folder somewhere on your computer ``python_lessons``, open your favourite text editor and type in the same command we used earlier ``print("Hello world!")`` then save your file and call it ``01_hello_world.py``

All python programs all end in `.py`  

The `01_` at the beginning is so all our files created in this tutorial are nicely sorted in a single folder

.. code-block:: console

    macbook ~ $ mkdir python_lessons
    macbook ~ $ cd python_lessons 
    macbook python_lessons $


And finally, execute this program by typing in *python* followed by the name of our file *01_hello_world.py*.

.. code-block:: console

    macbook python_lessons $ python 01_hello_world.py
    Hello world!
    macbook python_lessons $ _


You got lucky, you just wrote your first python program.

