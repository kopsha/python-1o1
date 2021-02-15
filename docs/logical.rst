******************
Logical operations
******************

Computers are funny creatures. They think in terms of *1*s and *0*s, *True* and
*False*. While Python has several numeric types, there is only one logical type:
*boolean*. A boolean can only take two values: **True** or **False**. And this
is all you need, **if** you are logical...


Bool type
#########

Booleans are a built-in data type in Python. Take care to note that *True* and
*False* are both capitalized.

.. code-block:: console

    >>> True
    True
    >>> true
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    NameError: name 'true' is not defined
    >>>


If you type it incorrectly, you will receive a name error.

Booleans are commonly encountered when comparing two objects. For example, to
compare two numbers use the *double equals* (``==``) operator:

.. code-block:: console

    >>> a = 3
    >>> b = 5
    >>> a == b
    False
    >>>

We get *False* since **a** and **b** are different integers. Notice that you use
one equal sign to assign numbers to a variabla, and a *double equal* sign to
compare them. In addition to testing if two numbers are the same you can test if
they are different usint the *not equal* operator.

.. code-block:: console

    >>> a != b
    True
    >>>

This comparison return *True* because it is true that *a does not equal b*. By
the way, the exclamation mark is commonly used as a logical **not** symbol in
programming languages. So this symbol literally reads as **not equal**.

And finally, in addition to comparing two numbers for equality or inequality,
you can test to see if one is larger than the other.

.. code-block:: console

    >>> a > b
    False
    >>> a < b
    True

    >>>

Is *a* greater than *b* ? No. This is a false statement.

Is *a* less than *b* ? Yes. This is a true statement.


Falsy values
^^^^^^^^^^^^

If you inspect the type of *True* and *False*:

.. code-block:: console

    >>> type(True)
    <class 'bool'>
    >>> type(False)
    <class 'bool'>
    >>>

You see the type is **bool**. This suggests another way to create booleans: by
passing values to the boolean constructor. For example, let's convert some
numbers to booleans:

.. code-block:: console

    >>> bool(28)
    True
    >>> bool(-2.71828)
    True
    >>> bool(0)
    False
    >>>

In Python, 0 is converted to *False*, while every other number is converted to
*True*.

We can also convert strings to booleans. For example,

.. code-block:: console

    >>> bool("Turing")
    True
    >>> bool(" ")
    True
    >>> bool("")
    False
    >>>

In Python, the empty string is converted to *False*, while every other string is
converted to *True*.

This is a general principle in Python. When converting a value to a boolean,
trivial values are converted to *False*, while non-trivial values are converted
to *True*.

Just as you can convert objects to booleans you can convert booleans to other
types of objects:

.. code-block:: console

    >>> str(True)
    'True'
    >>> str(False)
    'False'

If you convert *True* to a string, it returns **"True"**, but notice this is
surrounded by quotes, so it is a string. The boolean value does not have quotes.

You can also convert booleans to numbers. If you convert *True* to an integer,
you get **1** and if you convert *False* to an integer you get **0**.

.. code-block:: console

    >>> int(True)
    1
    >>> int(False)
    0
    >>> 5 + True
    6
    >>>

Look what happens if you add a number and a boolean: Python recognizez that you
are trying to add *True* to an integer, so it first converts it to an integer
then adds. What do you think **10 * False** will be ?

.. code-block:: console

    >>> 10 * False
    0
    >>>

Like before, Python recognizez you are trying to perform an arithmetic operation
so it converts *False* to the number 0 then multiplies. Is this something you
will use ? Probabily not. But it does highlight that Python treats 1 as True and
0 as False, and vice-versa. In computer science, this is a fundamental fact.


If statement
############

When coding in Python you will frequently encounter a fork in the road, depending
on the values of certain data you may want to go in one direction or the other,
there may be even more than two directions for you to choose, the if-then-else
statements help you navigate these situations:

	| **If** you want to learn more:
	| **then** continue reading this lesson
	| **else** try the next lesson.


if-then
^^^^^^^

In this example we will collect a string then test its length to see if it has
at least 8 characters. This is something you may need to do when validating new
passwords.

To begin, create a file called *if_then.py* and type in the following.

.. code-block:: python
	:emphasize-lines: 3

	password = input("Please enter a test string: ")

	if len(password) < 8:
		print("Your string is too short.")
		print("Please enter a string with at least 8 characters.")


The first line uses the ``input()`` function which will prompt the user to
enter a string and then store the value in the variable ``password``.

Next we use the **if-then** command to see if the length of the provided string
is less than 8 characters long. If *true* the following indented lines are
executed, if *not* these lines are skipped.

.. note ::

	Did you noticed that the **if** line ends with a colon (**:**) and the
	following lines are indented. This is how you identify *a code-block* in Python.
	This is a big difference from other languages such as Java or C++.

	In those languages indentation does not matter and you group code with braces,
	in Python you start a new code-block with a colon and group the commands with
	indentation. You can use any size indentation as long as the commands line up.

Now save this file and run the program from the command line and enter the word
*magic*.

.. code-block:: console

	$ python3 if_then.py
	Please enter a test string: magic
	Your string is too short.
	Please enter a string with at least 8 characters.
	$ _

Because this word has fewer than 8 characters the **if** statement is true (*the
length is less than 8*) so the following code-block is executed and the two lines
are printed.

Run the program again and enter a longer string like *fantastic*.

.. code-block:: console

	$ python3 if_then.py
	Please enter a test string: fantastic
	$ _

Because *fantastic* has more than 8 characters the **if** statement is false so
the following code-block is skipped.


if-then-else
^^^^^^^^^^^^

Let's see another example. Create a file called *if_then2.py*. This time we will
prompt the user to enter a number and we will test to see if it is even or odd.

First, the ``input()`` function returns a string, so we want to convert it to
an integer. We will do this using the ``int()`` constructor. If the user does
not type an integer this will cause an error. We will learn how to handle errors
in a future lesson.

.. code-block:: python
	:emphasize-lines: 4,6

	value = input("Please enter an integer: ")
	number = int(value)

	if number % 2 == 0:
		print("Your number is even.")
	else:
		print("Your number is odd.")

Next, if the **number** you entered is a multiple of two then print *Your number
is even.* else print *Your number is odd.*.

The ``%`` operator returns the remainder when you divide the first number by the
second one. In this case, we are computing the remainder when you divide the
number by 2. If the remainder is 0 then the number is even, otherwise it is odd.

We're ready to test this code, save the program and execute it in console.

.. code-block:: console

	$ python3 if_then2.py
	Please enter an integer: 17
	Your number is odd.
	$ _

Everything worked, the if-then statement correctly identified 17 as odd. Run the
program again and enter 50.

.. code-block:: console

	$ python3 if_then2.py
	Please enter an integer: 50
	Your number is even.
	$ _

Correct again.


if-elif-else
^^^^^^^^^^^^

For our final example we will create an if-then statement that
handles more than two cases. Create a file called *if_then3.py*. We will prompt
the user to enter the lengths of the sides of a triangle and we will determine
if it is scalene, isosceles or equilateral.

A scalene triangle is one where all three sides are different lengths, an
isosceles triangle has two sides of the same length and an equilateral triangle
is one where all the sides are equal.

First, we prompt the user to enter the lengths of the three sides. Like before,
we need to convert the strings to integers, we will do this in one line this time.

.. code-block:: python

	# scalene triangle: all three sides are different
	# isosceles triangle: two sides of the same length
	# equilateral triangle: all the sides are equal

	a = int(input("The length of side a: "))
	b = int(input("The length of side b: "))
	c = int(input("The length of side c: "))

	if a == b and b == c:
		print("This is an equilateral triangle.")
	elif a != b and b != c and a != c:
		print("This is a scalene triangle.")
	else:
		print("This is an isosceles triangle.")


Next, we compare the sides to determine the type of the triangle:

- if **a** equals **b** and **b** equals **c** then all three sides are identical, therefore it's an equilateral triangle
- if **a** does not equal **b** and **b** does not equal **c** and **a** does not equal **c** then all three sides are different, it's a scalene triangle
- if it is neither scalene nor equilateral then it must be an isosceles triangle.


.. note::

	This example illustrates how to handle more than two cases.
	Once again, if and else lines end in colons. The code-blocks that follow end
	in indentation.
	What's different is the use of ``elif`` which is short for ``else if``. This
	allows you to try another test. There is no limit on how many else ifs you
	can use.
	And finally the ``else`` statement is a catch-all, if all of the ifs above
	fail then this block is executed.

Let's test our code. Save the file and run it in console. Enter the sides: 3, 4
and 5:

.. code-block:: console

	$ python3 if_then3.py
	The length of side a: 3
	The length of side b: 4
	The length of side c: 5
	This is a scalene triangle.
	$ _

Our program is correct, a triangle with these sides is scalene. Run the program
again and enter: 5, 5 and 7:

.. code-block:: console

	$ python3 if_then3.py
	The length of side a: 5
	The length of side b: 5
	The length of side c: 7
	This is an isosceles triangle.
	$ _

Excellent, a triangle with these sides is definitely isosceles. One more, run the
program and enter: 4, 4, 4:

.. code-block:: console

	$ python3 if_then3.py
	The length of side a: 4
	The length of side b: 4
	The length of side c: 4
	This is an equilateral triangle.
	$ _

Perfect, these are the sides of an equilateral triangle. By the way, we did not
test the three numbers to make sure that they make a valid triangle. For example
you could enter negative integers and the program will still run.

Here's a problem for you to think about: how do you test three numbers to see if
they form a triangle?

The ``if``, ``elif`` and ``else`` statements allow you to handle any number of
cases in your code, they let you control the flow of your code.

	| *If* you are serious about programming in Python
	| *then* you should master these statements
	| or *else* ...


Conditional expressions
#######################

In Python, they are more commonly known as *ternary operators*. These operators
evaluate something based on a condition being true or not. Here you can see a
blueprint of using these conditional expressions:

.. code-block:: python

    value_for_true if condition else value_for_false

This allows you to shorten a multi-line if statement to a single line, making
your code compact but still readable. For example, let's determine whether the
water is solid (frozen) or liquid based on a temperature reading from an
external sensor and compare the :

.. code-block:: python

    temperature = -12  # external sensor reading

    # Using an if statement
    if temperature < 0:
        water_state = "solid"
    else:
        water_state = "liquid"

    # Using the ternary operator
    water_state = "solid" if temperature < 0 else "liquid"


Short-hand ternary
^^^^^^^^^^^^^^^^^^

In Python, there is also an even shorter version of the normal ternary operator
you have seen above. Its blueprint looks like this *value* **or** *alternative
value*, and this can allow you to easily provide a default value.

.. code-block:: python

    message = input() or "No data provided."
    print(message)

This is helpful in case you quickly want to check for the output of a function
or the input provided by the user and give a useful message if the value is
missing (actually if **bool(value) is False**).

