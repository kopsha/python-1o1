*********
Functions
*********

When programming, you will often encounter calculations and logical operations
you need to perform repeatedly. One way to handle this is to write the same code
over, and over, and over... A better solution is to write a *function*.

Functions enable you to reuse logic an infinite number of times without
repeating yourself. This is especially helpful to avoid moments of deja vu.

A better solution is to write a *function*. Functions enable you to reuse logic
an infinite number of times without repeating yourself. This is especially
helpful... to avoid...  moments of deja vu.


Define
######

To define a function, you write **def** followed by the name of the function.
We will call this function **f**. Next, you write parentheses. Inside the
parentheses you list the inputs to the function. Another name for *inputs* is
*arguments*.

.. code-block:: python

    def f():
        pass

This function has 0 arguments.  For our first function, we will keep things
simple. We will *pass*. The word *pass* is how you tell Python to skip this line
and do nothing.

.. tip::

    The colon is how you start a new code block in Python. Notice that we
    indented the code inside the function. Python requires you to group code
    blocks by indentation.

There we have created our first function. It is short, it is simple. But does it
work ?

To *run* the function (in programming we say *call the function*), type the name
and parentheses...

.. code-block:: console

    >>> f()
    >>>

The function **f** did nothing, just like we told it to. By the way, look what
happens if you forget to type parentheses.

.. code-block:: console

    >>> f
    <function f at 0x101241a60>
    >>>

Without parentheses, Python displays that **f** is a function and gives the
memory address. Interesting, but not very helpful. You need to include
parentheses to actually call the function.



Return
######

Now, we will write a function that actually does something. We'll name this
function **ping**. This function will have 0 arguments. Functions in Python can
return values. To return a value, type the word **return** and then the object.
This function will return the string **"Ping"**, and to show our enthusiasm,
we will add an exclamation point.

.. code-block:: python

    def ping():
        return "Ping!"

Return values are optional, you are under no obligation to return something. Now
call the function.

.. code-block:: console

    >>> ping()
    'Ping!'
    >>>

This function return the string **"Ping!"**. Since we did not assign this to a
variable, Python printed it to the terminal. But we can also store the return
value to a variable. To see that this worked, print the value of **x**.

.. code-block:: console

    >>> x = ping()
    >>> print(x)
    Ping!


Arguments
#########

For our next example, recall that the volume of a sphere is

.. math::

    V =  \frac{4}{3} \pi r^3

Where *r* is the radius of the sphere. We will write a function which will
return the volume of a sphere when given the radius. To do this, we will need
to use the number *pi* (:math:`\pi`). This is available in Python, but first
you must import the *math* module.

We will call this function *volume*. This function will have a single argument:
the radius **r**. Next, we will write a brief comment describing this function.
This is called a **docstring** and provides documentation on what the function
does and how to use it.

.. code-block:: python

    import math

    def volume(r):
        """Returns the volume of a sphere with radius r."""
        v = (4/3) * math.pi * r**3
        return v

Notice that we used a double asterisk (``**``) for exponents. Let's test this function. Compute the volume of a sphere with radius 2.

.. code-block:: console

    >>> volume(2)
    33.510321638291124
    >>>

Because we used an argument when defining the function, you must provide an
input when calling it. **r** is a required argument. Look what happens if you
call *volume* without an argument.

.. code-block:: console

    >>> volume()
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: volume() missing 1 required positional argument: 'r'
    >>>

You get an error and a reminder to use an argument. We can use the help function
to see how to use the volume function.

.. code-block:: console

    >>> help(volume)
    Help on function volume in module __main__:

    volume(r)
        Returns the volume of a sphere with radius r.


We have created functions with no arguments and with one argument. We will now
throw caution into the vacuum of space and write a function with two arguments.
Our function will compute the area of a triangle. Recall that the area of a
triangle is

.. math::

    V &= \frac{1}{2} base \times height

Our previous function was named *volume*, which was somewhat vague. The name
does not tell you what shape is being considered. This time we will be more
explicit and name the function **triangle_area**. To compute the area, we need
two arguments: the base **b** and the height **h**. Write a *docstring* giving
a brief description of this function and finally return the area of the triangle.

.. code-block:: python

    def triangle_area(b, h):
        """Returns the area of a triangle with base b and height h."""
        return 0.5 * b * h

We are ready to test the function.

.. code-block:: console

    >>> triangle_area(3, 6)
    9.0
    >>>


There is no limit to how many arguments you can use in your function, but if the
number of inputs is too large, you will alienate other and receive accusing
glares...


Keyword arguments
#################

Functions in Python can accept another kind of argument called *keyword
arguments*. To show how to use these kinds of arguments, we will write a
function which convers a person's height from imperial units, feet and inches to
centimeters.

Recall that :math:`1 inch = 2.54 cm` and :math:`1 foot = 12 inches`.

We'll name this function **cm**, for centimeters. This function will accept two
arguments: **feet** and **inches**. Next, add a *docstring* describing the
function.

.. code-block:: python

    def cm(feet = 0, inches = 0):
        """Converts a length from feet and inches to centimeters."""
        inches_to_cm = inches * 2.54
        feet_to_cm = feet * 12 * 2.54
        return inches_to_cm + feet_to_cm

Notice that the arguments have equal signs after them. It looks as we are
assigning values to these arguments. In fact, we are. We are assigning a default
value of 0 to each argument. For this reason, Python also calls keyword
arguments *default arguments*.

We could have combined all computations on one line, but it is better to write
clean code which is easy to read, as opposed to compact code which impresses no
one.

Here is how you call a function with keyword arguments:

.. code-block:: console

    >>> cm(feet = 5)
    152.4
    >>> cm(inches = 70)
    177.8
    >>> cm(feet = 5, inches = 8)
    172.72
    >>>

We can also perform this last calculation by specifying inches first:

.. code-block:: console

    >>> cm(inches = 8, feet = 5)
    172.72
    >>>

Keyword arguments help you to write flexible functions and clean code.


There are two kinds of arguments you can use when writing a function. A keyword
argument (or default argument), which has an equal sign, and a required argument
which does not have an equal sign. When writing a function, you can use both
kinds of arguments. But if you do this, the keyword arguments must come last.

For example, if you define a function **g** with a keyword argument first, you
get a syntax error.

.. code-block:: console

    >>> def g(x = 0, y):
    ...     return x + y
    ...
      File "<stdin>", line 1
    SyntaxError: non-default argument follows default argument
    >>>

Notice that Python calls these *default argument*. This is another name for a
*keyword argument*. To fix this, you have to list non-default arguments first.
These are also called *required arguments* since they are required.

.. code-block:: console

    >>> def g(y, x = 0):
    ...     return x + y
    ...
    >>> g(7)
    7
    >>>

To call this function, you must pass in a value for the required argument **y**.
The keyword argument **x** is optional. If you do not provide a value for x, the
default value is used.

If you want to pass in a value for the keyword argument, then you must specify
it by its name. Required arguments are not given a name. They are determined by
their position.

.. code-block:: console

    >>> g(7, x=3)
    10
    >>>

Functions in Python are flexible contraptions. Required arguments, keyword
arguments, docstrings, return values -- together they empower you to write some
amazing, reusable code. And if your function does not require an input, you will
not get an argument from me...


Exercises
#########

1. Calculate the factorial of a number (positive integer).

#. Write a function that flattens a list. (Remember that a list may contain an
element which is in fact another list)

#. Generate a list with Fibonacci sequence up to a number.

#. Generate a list with all prime numbers less than a number.

