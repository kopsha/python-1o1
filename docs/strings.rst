*******
Strings
*******


When programming, text is represented by strings. In Python there are many ways
to create a string, after all there are many different types of text. Some have
apostrophes, some have quotation marks and some long strings have new lines.

Your goal today: make strings in three different ways.


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

