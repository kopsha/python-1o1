*******
Strings
*******


When programming, text is represented by strings. In Python there are many ways
to create a string, after all there are many different types of text. Some have
apostrophes, some have quotation marks and some long strings have new lines.

Your goal today: make strings in three different ways.


Create strings
##############

First, we create a string a store it in a variable:

.. code-block:: python

	message = "Meet me tonight."

This stores the string *Meet me tonight.* in a variable called *message*. You do
not have a type a semicolon at the end like you do in many other languages like
Java or C++. You can see the string stored in *message* by printing it:


.. code-block:: python

	>>> message = "Meet me tonight."
	>>> print(message)
	Meet me tonight.
	>>> _

We've created our first string using quotation marks, but you can also create
strings using single quotes:

.. code-block:: python

	>>> another_message = 'The clock strikes at midnight.'

Let's verify the text stored in this new variable by printing it:

.. code-block:: python

	>>> print(another_message)
	The clock strikes at midnight.

So you can create strings using single quotes (**'**) or double quotes (**"**),
we did not had to specify that *message* or *another_message* were strings, we
just assign them strings and Python was smart enough to know that the variables
should hold strings. But what's the point of this, to have more than one way to make a string? 

Well, suppose you want to make a string and one of the words had an apostrophe,
if you try to make the string using single quotes you'll get a syntax error

.. code-block:: python

	>>> message2 = 'I'm looking for someone to share an adventure.'
	  File "<stdin>", line 1
	    message = 'I'm looking for someone to share an adventure.'
	                 ^
	SyntaxError: invalid syntax
	>>> 

Do you see the problem ?
When Python encountered the apostrophe in the word *I'm* it thought that it was
the end of the string so the remaining text caused the error. There are two ways
to fix this.

One way is to escape the apostrophe, by putting a backslash (\) in front of it.

.. code-block:: python

	>>> message2 = 'I\'m looking for someone to share an adventure.'
	>>> 

This tells Python that the single quote is to be treated as a single character
and not the end of the string, but the savvy way is to create the string using
quotation marks:

.. code-block:: python

	>>> message3 = "I'm looking for someone to share an adventure."
	>>> 

No errors, no escape characters.

If you make a string using double quotes but your text contains a quotation mark
you get another error:

.. code-block:: python

	>>> message4 = "The phrase "Beam me up, Scotty!" was never said on Star Trek."
	  File "<stdin>", line 1
	    message4 = "The phrase "Beam me up, Scotty!" was never said on Star Trek."
	                               ^
	SyntaxError: invalid syntax
	>>> 

This is because Python interprets the quotation mark before the word *Beam* as
the end of the string. We can avoid this error by using single quotes to make
the string.

.. code-block:: python

	>>> message4 = 'The phrase "Beam me up, Scotty!" was never said on Star Trek.'
	>>>


But how do you make more complicated strings, which may contain apostrophes and
quotation marks? For this case you cand begin and end the string using triple quotes. You can use
three double quotes or three single quotes. We'll use double quotes:

.. code-block:: python

	>>> movie_quote = """One of my favourite lines from The Godfather is:
	... "I'm going to make him an offer he can't refuse."
	... Do you know who said this?"""
	>>> 

This text has single quotes, double quotes and even new lines.

.. admonition:: Did you notice?

	The triple dots which appeared while typing this?
	That's how Python tells you the command you're typing is taking more than one line.


So you can create strings in Python using single quotes, double quotes or triple
quotes. This makes it easy to store all kinds of texts without having to resort
to trickery and you can quote me on that.


Operators
#########

You have already seen the operators + and * applied to numbers. These two
operators can be applied on strings as well.


The + operator
**************

The + operator concatenates strings. It returns a string consisting of the
operands joined together, as shown here:

.. code-block:: python

	>>> s = 'foo'
	>>> t = 'bar'
	>>> u = 'baz'
	>>> s + t
	'foobar'
	>>> s + t + u
	'foobarbaz'
	>>> print('Go team' + '!!!')
	Go team!!!


The * operator
**************

The * operator creates multiple copies of a string. If s is a string and n is
an integer, either of the following expressions returns a string consisting of
n concatenated copies of s:

.. code-block:: python

	>>> s = 'foo.'
	>>> s * 4
	'foo.foo.foo.foo.'
	>>> 4 * s
	'foo.foo.foo.foo.'

The multiplier operand n must be an integer. You’d think it would be required
to be a positive integer, but amusingly, it can be zero or negative, in which
case the result is an empty string:

.. code-block:: python

	>>> 'foo' * -8
	''

If you were to create a string variable and initialize it to the empty string by
assigning it the value 'foo' * -8, anyone would rightly think you were a bit
daft. But it would work.


The in Operator
***************

Python also provides a membership operator that can be used with strings.
The in operator returns True if the first operand is contained within the second,
and False otherwise:

.. code-block:: python

	>>> s = 'foo'
	>>> s in "That's food for thought."
	True
	>>> s in "That's good for now."
	False

There is also a not in operator, which does the opposite:

.. code-block:: python

	>>> 'z' not in 'abc'
	True
	>>> 'z' not in 'xyz'
	False


Built-in functions
##################

Python provides many functions that are built-in to the interpreter and always
available. Here are just a few that work for strings:

- ``len()`` returns the length of a string
- ``str()`` returns a string representation of an object
- ``lower()`` converts alphabetic characters to lowercase
- ``upper()`` converts alphabetic characters to uppercase


len()
*****

Returns the length of a string.

With **len()**, you can check Python string length. **len(s)** returns the number of characters in s:

.. code-block:: python

	>>> s = 'I am a programmer.'
	>>> len(s)
	18


str()
*****

Returns a string representation of an object.

Virtually any object in Python can be rendered as a string. **str(x)** returns
the string representation of variable or expression **x**:

.. code-block:: python

	>>> str(49.2)
	'49.2'
	>>> str(3+4j)
	'(3+4j)'
	>>> str(3.21 + 29)
	'32.21'
	>>> str('to the moon and back')
	'to the moon and back'


lower()
*******

Given a variable named s holding a string, by typing ``s.lower()`` you will get
a copy of s with all alphabetic characters converted to lowercase:

.. code-block:: python

	>>> s = "NYSE News: What happened to Google stocks price?"
	>>> s.lower()
	'nyse news: what happened to google stocks price?'


upper()
*******

``s.upper()`` returns a copy of **s** with all alphabetic characters converted to uppercase:

.. code-block:: python

	>>> s = "I want an expresso."
	>>> s.upper()
	'I WANT AN EXPRESSO.'

A line of text in all caps looks like someone is yelling.


f-Strings
#########

Also called *formatted string literals*, f-strings are string literals that have
an **f** at the beginning and *curly braces* inside containing expressions that
will be replaced with their values.

Here are some of the ways f-strings can make your life easier.

.. code-block:: python

	>>> name = "Eric"
	>>> age = 24
	>>> f"Hello, {name}. You are {age} years old or {age * 12} months old."
	'Hello, Eric. You are 24 years old or 288 months old.'

Look how easy it is to read or predict how it will look.
