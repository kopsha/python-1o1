*********
JSON data
*********

JSON (*JavaScript Object Notation*) is a small lightweight, data format. A packet
of JSON data is almost identical to a Python *dictionary*. It is shorter than
XML and can be quickly parsed by humans and most importantly any web browsers
since it uses JavaScript syntax. This makes JSON an ideal format for transporting
data between a client and a server. If your client is not a browser, don't worry.
Android, iOS and other mobile operating systems, all come equipped with tools for
parsing and working with JSON.

In this lesson I will show you how to use Python's built-in JSON library to send
and receive JSON data.


A Little Vocabulary
###################

The process of encoding JSON is usually called *serialization*. This term refers
to the transformation of data into *a series of bytes* (hence serial) to be
stored or transmitted across a network. You may also hear the term *marshaling*,
but that’s a whole other discussion.

Naturally, *deserialization* is the reciprocal process of decoding data that has
been stored or delivered in the JSON standard.

    Yikes! This sounds pretty technical. Definitely. But in reality, all we’re
    talking about here is *reading* and *writing*. Think of it like this:
    encoding is for writing data to disk, while decoding is for reading data
    into memory.


Simple Python objects are translated to JSON according to a fairly intuitive
conversion:

==================  ======
Python	            JSON
==================  ======
dict	            object
list, tuple         array
str	                string
int, long, float	number
True	            true
False	            false
None                null
==================  ======


Compare to XML
**************

Here is a typical JSON data packet.

.. code-block:: javascript

    {
        "title": "Gattaca",
        "release_year": 1997,
        "is_awesome": true,
        "won_oscar": false,
        "actors": ["Ethan Hawke", "Uma Thurman", "Alan Arkin", "Loren Dean"],
        "budget": null,
        "credits": {
            "director": "Andrew Niccol",
            "writer": "Andrew Niccol",
            "composer": "Michael Nyman",
            "cinematographer": "Slawomir Idziak"
        }
    }

This JSON object contains examples of all possible data types. All the keys are
*strings*, but the values can be *strings*, *numbers*, *booleans*, *list*, *null*
or even another JSON object.

Now, compare it with the XML version:

.. code-block:: XML

    <?xml version="1.0" encoding="UTF-8"?>
    <root>
    <actors>
        <element>Ethan Hawke</element>
        <element>Uma Thurman</element>
        <element>Alan Arkin</element>
        <element>Loren Dean</element>
    </actors>
    <budget null="true" />
    <credits>
        <cinematographer>Slawomir Idziak</cinematographer>
        <composer>Michael Nyman</composer>
        <director>Andrew Niccol</director>
        <writer>Andrew Niccol</writer>
    </credits>
    <is_awesome>true</is_awesome>
    <release_year>1997</release_year>
    <title>Gattaca</title>
    <won_oscar>false</won_oscar>
    </root>

The increased size of the XML data is largely due to the end tags repeating the
text of the openning tags. A popular sport is debating the merits of JSON versus
XML. But instead of arguing, I recommend you learn the pros and cons of both
formats, then choose the one which is best for your project.


Reading JSON
############

First, let's save the sample JSON data to a text file, and then we'll use the
context manager to open up the existing ``data_file.json`` in read mode.

The **json** library provides two methods for turning JSON encoded data into
Python objects:

- the *load()* method allows to read (load) JSON data directly from a file
- while the *loads()* methods allows to read (load) JSON data from a string.

    That's why there is an extra *s* in the method name, *s* for *string*.


Now, let's load the JSON data, from the file created earlier, using the *load()*
method.

.. code-block:: python

    import json

    with open("data_file.json", "rt") as data_file:
        data = json.load(data_file)

If you display the object you will see a dictionary containing all the data:

    >>> print(data)
    {'title': 'Gattaca', 'release_year': 1997, 'is_awesome': True, 'won_oscar': False, 'actors': ['Ethan Hawke', 'Uma Thurman', 'Alan Arkin', 'Loren Dean'], 'budget': None, 'credits': {'director': 'Andrew Niccol', 'writer': 'Andrew Niccol', 'composer': 'Michael Nyman', 'cinematographer': 'Slawomir Idziak'}}
    >>> type(data)
    <class 'dict'>
    >>>

If you look at the type, you will see it is, in fact, a dictionary. Also, notice
how the *true*, *false* and *null* were correctly parsed into Python's *True*,
*False* and *None*.

Because this is a dictionary, you can access the data by key. We can see the
title, the list of actors and so on:

    >>> data["title"]
    'Gattaca'
    >>> data["actors"]
    ['Ethan Hawke', 'Uma Thurman', 'Alan Arkin', 'Loren Dean']
    >>> data["release_year"]
    1997
    >>>

