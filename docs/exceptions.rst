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


Traceback
#########

To illustrate the exceptions I am going to deliberately make mistakes in my code.
The mere thought of this causes my neural nets to rebel, but this is for a good
cause.

Let us first write some code to print ``Hello, world!`` three times:

.. code-block:: python

    for i in range(3)
        print("Hello, world!")

Then run:

.. code-block:: console
    :linenos:
    :emphasize-lines: 2,3,5

    macbook$ python3 mistakes.py
    File "/Users/fleorin/src/python-1o1/examples/mistakes.py", line 1
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

Let us see a few more common exceptions before we learn how to raise and handle
them. We'll try to open the **"x-files.txt"** and read it. This will be exciting
to read.

.. code-block:: python

    with open("x-files.txt") as textfile:
        the_truth = textfile.read()
    print(the_truth)

Why am I not surprised::
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

.. tip:: Built-in exceptions

    Python comes with a large collection of `built-in exceptions <https://docs.python.org/3/library/exceptions.html#exception-hierarchy>`.
    Here you can explore them organized in a logical hierarchy.
    Notice how most of these class names end in **Error** and not in
    **Exceptions**, like in many other languages.


Handling exceptions
###################

The general way for handling exceptions is the **try / except / else / finally**
construction::
    try:
        ...
    except:
        ...
    else:
        ...
    finally:
        ...

