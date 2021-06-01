**********
Exceptions
**********

Long before the computing era, Benjamin Franklin once said: *"If you fail to
plan, you are planning to fail."*
As you may have already noticed, when running computer programs, something
unexpected always happens. Even when they are really simple, like the ones in
these lessons: maybe a file is not there when you try to read it, or you type a
string where a number was needed or simply you press *<Enter>* when you should
have entered some text.

If there is a way for code to break, then somehow, somewhere, someone will break
it. Using *exceptions* you can manage these problems in a responsible way: if a
client asks you to capitalize an integer you can decline their bizarre
suggestion. Once you learn how to do this, you will become an exceptional Python
programmer.

An *exception* is an error that is *raised* by Python, when the execution of our
code results in an unexpected outcome. Normally, an exception will have a *type*
and a *message*. For example, when python prints such exceptions::

    ZeroDivisionError: division by zero
    TypeError: must be str, not int
    IndexError: list index out of range

The **ZeroDivisionError**, **TypeError** and **IndexError** represent the *error
type* and the text that follows the colon is the *error message*. This message
usually describes the cause of the error in more detail and/or the expected vs.
actual input.


The traceback
#############

To illustrate the exceptions I am going to deliberately make mistakes in my code.
The mere thought of this causes my neural nets to rebel, but this is for a good
cause.

Let us first write some code to print ``Hello, world!`` three times:

.. code-block:: python

    for i in range(3)
        print("Hello, world!")

Then run:

.. code-block:: console
    :emphasize-lines: 2,3

    macbook$ python3 mistakes.py
    File "/Users/python-1o1/examples/mistakes.py", line 1
        for i in range(3)
                        ^
    SyntaxError: invalid syntax


Instead of our welcoming, we see a problem: the last line displays the error
type and also a description. A **syntax error** means you did not follow the
rules for how to write valid Python code. You will encounter this a lot when
you're first learning Python. Above you will see some text that tells you where
the problem occurred, this text is called a **traceback**. Here, we're missing
a colon at the end of the for loop, if we correct and run again everything works
as expected::
    Hello, world!
    Hello, world!
    Hello, world!


Common exceptions
#################

Let us see a few more common exceptions before we learn how to raise and handle
them. Open the **x-files.txt** and read it. This should be exciting to read.

.. code-block:: python

    with open("x-files.txt") as textfile:
        the_truth = textfile.read()
    print(the_truth)

Why am I not surprised:

.. code-block:: console

    Traceback (most recent call last):
    File "/Users/python-1o1/examples/mistakes.py", line 4, in <module>
        with open("x-files.txt") as textfile:
    FileNotFoundError: [Errno 2] No such file or directory: 'x-files.txt'

Whenever we try to read a non-exitent file Python raises a **FileNotFoundError**.
The truth must still be out there.

What if you try to add one, two and three but instead of the number 3 you use
the word **three**::
    >>> 1 + 2 + "three"
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    TypeError: unsupported operand type(s) for +: 'int' and 'str'
    >>>

How I laughed while typing that. Here you get a **TypeError** with a more helpful
description. Python lets you know that you cannot add an integer and a string.
This exception is very common, it occurs when you expect one type of data but
receive another.

.. code-block:: python

    first_name = "Benjamin"
    print(fist_name)

.. code-block:: console

    Traceback (most recent call last):
    File "/Users/python-1o1/examples/mistakes.py", line 5, in <module>
        print(fist_name)
    NameError: name 'fist_name' is not defined

The **NameError** exception is thrown whenever we try to use a variable that does
not exist, or a function that was not defined. The error message is quite clear,
you should be able to fix it easily. Most often there is a misspelled name or a
missing import.


Handling exceptions
###################

Python provides us with the **try except** construction to handle exceptions that
might be raised by our code. The basic anatomy of the **try except** clause is as
follows

.. code-block:: python

    try:
        # this code runs first
        ...
    except:
        # runs when the code above fails
        ...

In plain English, the try except clause is basically saying: *Try to do this,
except if there’s an error, then do this instead*.

There are a few options on what to do with the thrown exception from the try
block. Let’s discuss them.


Catch specific exceptions
#########################

Python allows us to define which exception types we want to *catch* explictily.
To do this, we need to specify the type to the **except** block.

.. code-block:: python

    a = 42
    b = "ten"
    try:
        sum = a + b
    except TypeError:
        print("Cannot sum the variables, please pass numbers only.")

And when we run this code we get:

.. code-block:: console

    macbook$ python3 mistakes.py
    Cannot sum the variables, please pass numbers only.

It is starting to look better, isn't it? Now, we can actually **log** or **print**
the exception itself:

.. code-block:: python

    a = 42
    b = "ten"
    try:
        sum = a + b
    except TypeError as err:
        print(f"Cannot sum the variables, reason: {err}.")

.. code-block:: console

    macbook$ python3 mistakes.py
    Cannot sum the variables, reason: unsupported operand type(s) for +: 'int' and 'str'.

Furthermore, we can catch multiple exception types in one clause if we want to
handle them in the same way:

.. code-block:: python

    a = 42
    b = 10
    try:
        sum = a + b + c
    except (TypeError, NameError) as err:
        print(f"Cannot sum the variables, reason: {err}.")

.. code-block:: console

    macbook$ python3 mistakes.py
    Cannot sum the variables, reason: name 'c' is not defined.

Basically, we just need to pass a **tuple** containing the exception types that
we need to handle.

Sometimes, we may need another **except** block with no specific exception type.
The purpose of this is to catch all exception types. A typical use case would be
when making a request to a third party API, we might not know all of the possible
exception types, however, we still want to catch and handle them all.

.. code-block:: python

    a = 42
    b = 10
    c = 0
    try:
        remainder = (a + b) % c
    except (TypeError, NameError) as err:
        print(f"Cannot compute the result, reason: {err}.")
    except Exception as err:
        print(f"A {type(err)} occurred, please inspect: {err}.")

.. code-block:: console

    macbook$ python3 mistakes.py
    A <class 'ZeroDivisionError'> occurred, please inspect: integer division or modulo by zero.

In the case our code raises any exceptions other than TypeError and NameError,
it will run last except block and print the message.

Notice that we used the **Exception** keyword to specify the generic error type
that will match any exceptions.

.. seealso::

    Python comes with a large collection of `built-in exceptions
    <https://docs.python.org/3/library/exceptions.html#exception-hierarchy>`_.
    Here you can explore them organized in a logical hierarchy.
    Notice how most of these class names end in **Error** and not in
    **Exceptions**, like in many other languages.

Just so you know, we can still extend our try except clause by adding **else**
and **finally** blocks to it. More on this in a future lesson. Or if you want to
read about it yourself, you can checkout the official `documentation
<https://docs.python.org/3/tutorial/errors.html#handling-exceptions>`_.
