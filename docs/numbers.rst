*******
Numbers
*******


Among other many other things, Python understands numbers. Let's open the python interpretor console and try them out.

.. code-block:: console

    Python 3.7.2 (default, Dec 27 2018, 07:35:52) 
    [Clang 10.0.0 (clang-1000.11.45.5)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>> 10
    10
    >>> 10 + 5  
    15
    >>> 1.5 * 2
    3.0
    >>> 

In Python 3 there are three types of numbers, in Python 2 there are four types of number. And if you're using C++ then you will be glad that you're learning Python.

You can inspect the type of any number, variable, string or even expressions by using the function ``type()``.

int
###

The first type of numbers in python is ``int``, which is short for *integer* or
numbers without a decimal point.

.. code-block:: console

    Python 3.7.2 (default, Dec 27 2018, 07:35:52) 
    [Clang 10.0.0 (clang-1000.11.45.5)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>> 42 # is an integer
    42
    >>> type(42)
    <class 'int'>
    >>> perfect_number = 28     # let's assign the value 28 to a variable named perfect_number
    >>> type(perfect_number)
    <class 'int'>
    >>> perfect_number
    28
    >>> # or, if you love typing, you can print it explicitly
    ... print(perfect_number)
    28
    >>> _


.. tip:: the hash tag
    is how your write comments in Python. Everything after a hashtag ``#`` is ignored by the interpreter. This can be extremely useful to explain something in your code which may not be obvious for your colleagues.

In Python 3 you don't have to worry about the size of an integer. You can create integers of any size provided your computer is large enough store it.

No size limits, no overflows, no worries.


float
#####

The second type of numbers in Python 3 is *float*. This is how decimal values are stored. To make a float, just type in a number that has a decimal point. We'll use the famous number *e* which is approximately 2.718281828.

To confirm that this is a float, look at its type:

.. code-block:: console

    >>> e = 2.718281828
    >>> type(e)
    <class 'float'>
    >>> e
    2.718281828
    >>> 


complex
#######

The third type of numbers in python is *complex numbers*.

Complex numbers are an extension of the familiar real number system in which all numbers are expressed as a sum of a *real* part and an *imaginary* part.

Imaginary numbers are real multiples of the *imaginary unit* (the square root of -1), often written *i* in mathematics or *j* in engineering.

Python has built-in support for complex numbers, which are written with this latter notation; the imaginary part is written with the letter *j* as suffix, e.g. ``3+1j``.

Again, you can confirm that this is a complex number by checking its type:

.. code-block:: console

    >>> z = 2 + 3j
    >>> z    
    (2+3j)
    >>> type(z)
    <class 'complex'>
    >>> _

You can also display the real and imaginary parts separetely. To access the real part you can use the ``.real`` property (notice the dot) and you can access the imaginary part through the ``.imag`` property.

.. code-block:: console

    >>> z = 2 + 3j
    >>> z.real
    2.0
    >>> z.imag
    3.0
    >>> _

Did you noticed that even that the real part is a float while we typed it as an integer. This is because Python stores the real and imaginary part of complex numbers as floats.

Now that you know about ``int``, ``float`` and ``complex`` numbers you are ready to tackle arithmetic.

Just remember:

* the mathematical *i* is called *j*,
* complex numbers are made of *floats*
* the ``type()``  function can tell you what type of numbers you really have
 

Type conversion
###############

Whenever you write an arithmetic expression Python converts numbers internally
in an expression containing mixed types to a common type for evaluation.
But sometimes, you need to convert a number explicitly from one type to another:

- type ``int(x)`` to convert x to a plain integer
- type ``float(x)`` to convert x to a floating-point number
- type ``complex(x)`` to convert x to a complex number with real part x and imaginary part zero
- type ``complex(x, y)`` to convert x and y to a complex number with real part **x** and imaginary part **y**, where **x** and **y** can be numeric expressions
