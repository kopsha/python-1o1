***********
First Steps
***********

It has become a programmer tradition that when you learn a new programming
language, you start with a simple program that only says "hello world".

*A way to show the world that we are civil*.

We will now see how to run a traditional 'Hello World' program in Python. This
will teach you how to *write* and then *run* Python programs.

There are two ways of using Python to execute your program:

- using the interactive interpreter prompt, or
- using a source file.

We will now see how to use both of these methods.



Using The Interpreter Prompt
############################

First we need to verify if python is installed on our computer by opening the
``terminal`` application (for Windows users, type Win+R and then `cmd`).

Type in `python3` and see what happens
    
.. code-block:: console

    $ python3
    Python 3.7.2 (default, Dec 27 2018, 07:35:52) 
    [Clang 10.0.0 (clang-1000.11.45.5)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>> _

If you see a version number and a ``>>>`` prompt, you're good to go. But if you
see an error, you need to download and install python. I recommend to visit
the `python comunity website <http://www.python.org/>`_ and download the latest
python3 version.

Let's get more familiar with the python interpreter. The easiest way you can
interact with the python interpreter is through this console. Here you can
*talk* directly to the core of python and send your request.

Once you have started Python, you should see ``>>>`` where you can start typing
stuff. This is called the Python interpreter prompt.

At the Python interpreter prompt, type:

.. code-block:: console

    print("Hello World")

followed by the [enter] key. You should see the words ``Hello World`` printed
on the screen.

Here is an example of what you should be seeing, when using a Mac OS X computer.
The details about the Python software will differ based on your computer, but
the part from the prompt (i.e. from ``>>>`` onwards) should look the same
regardless of the operating system you are using.

.. code-block:: console

    $ python3
    Python 3.7.2 (default, Dec 27 2018, 07:35:52) 
    [Clang 10.0.0 (clang-1000.11.45.5)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>> print("Hello World")
    Hello World

Notice that Python gives you the output of the line immediately! What you just
entered is a single Python statement. We use print to (unsurprisingly) print any
value that you supply to it. Notice, that we are supplying the text "Hello World"
and this is promptly printed to the screen.


How to Quit the Interpreter Prompt
**********************************

If you are using a GNU/Linux or OS X shell, you can exit the interpreter prompt
by pressing [ctrl + d] or entering exit() (note: remember to include the
parentheses, **()**) followed by the [enter] key.

If you are using the Windows command prompt, press [ctrl + z] followed by the [enter] key.



Python as an interactive calculator
***********************************

To get your feet wet with Python you can use the Python interpreter as a
calculator. You have the usual mathematical operators at your disposal, like

- ``+`` addition,
- ``-`` subtraction,
- ``*`` multiplication,
- ``/`` division,
- ``**`` exponent,
- ``//`` integer division, and
- ``%`` modulus.

If you are not familiar with one of them just give it a try in the Python
interpreter -- python does not limit you to integer numbers, feel free to
try also floating point numbers or even strings.

You can also use brackets as you would use them in mathematical expressions.

Can you find out whether Python uses the proper mathematical rules with regards
to the order of execution of the operators.

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

Observe that python tries to *understand* what we type, be it numbers,
arithmetic operations or strings, computes the result and prints it back for us.
However, if we accidentally type something that doesn't make sense, *Python*
will do its best to point out the problem, but it will let us decide how and
when we'll fix it.


The ``print()`` function
************************

When you are typing expresions in the python interpreter (remember the ``>>>``
prompt?) they are evaluated and the result is being printed on the screen for us.
But when you are running the python program (see below) you need to be explicit
to python about when to display an actual value or an expression.

The function you used in your first program, the ``print(...)`` function,
behaves almost the same as the interpreter, it looks at our input, be it
numbers, text, expression or even other functions, tries to understand it,
evaluates tem and then shows the result on the screen.



Using a source file
###################

Besides the interactive Python interpreter you can also write Python programs
(sometimes called scripts). A python program is a file that contains a list of
python *expressions* or *statements* that can be executed from the command line.
A script can be really simple e.g. searching a text inside a file or it could be
as complex as a car crash simulation.

Now we'll say *hello* using a python program instead of the interactive console,
so exit python by typing ``quit()``

.. code-block:: console

    >>> quit()
    macbook$ _

Create a folder somewhere on your computer ``python_lessons``, open your
favourite text editor and type in the same command we used earlier
``print("Hello world!")`` then save your file and call it ``01_hello_world.py``

All python programs are files whose names end in **.py**.

The **01_** at the beginning is so all our files created in this tutorial are
nicely sorted in a single folder.

.. code-block:: console

    macbook ~ $ mkdir python_lessons
    macbook ~ $ cd python_lessons 
    macbook python_lessons $

And finally, execute this program by typing in **python3** followed by the name
of our file **01_hello_world.py**.

If you did everything correctly then your console should look like this:

.. code-block:: console

    macbook python_lessons $ python 01_hello_world.py
    Hello world!
    macbook python_lessons $ _


You got lucky, you just wrote your *first python program*.


Choosing and editor
###################

Now, that you've entered the world of python programming you may want to take it
to the next level by using a text editor that was designed for editing python
programs.

Even though there are many options available, I recommend you these two:

.. admonition::  sublime text

    is easier to use, it has all the features you may want and you don't event know them yet; it is light, fast and has a beautiful color theme.
    Long story short: it is *sublime*.

    You can get it from the `sublimetext website <https://www.sublimetext.com/3>`_

    And if you need any help have a look a this `video tutorial <https://www.youtube.com/watch?v=SVkR1ZkNusI>`_.


.. admonition::  pycharm

    is just a bloated version of *sublime text* with the advantage that you
    could execute your programs directly in the editor or just line-by-line
    (read as *debug your code*) which could be useful when learning python to
    understand how complex structures are being executed.

    You can get it from `jetbrains website <https://www.jetbrains.com/pycharm/>`_.

    It also has an `educational version <https://www.jetbrains.com/education/#lang=python&role=learner>`_.


Exercise
########

Write a program that given the radius of a circle it computes the circumference and the area.
You will need to use the ``pi``, so please define it as: 

.. code-block:: python

    pi = 3.141592653589793


*The End*
