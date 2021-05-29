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

    That's why there is an extra **s** in the method name: *s* for *string*.


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

Now, let's focus on the **loads()** method, which must be used if the data you
need to process arrives in the form of a string. This is common in client-server
applications where data is sent over the internet. As an illustration let's create
a string with a JSON formatted value:

.. code-block:: python

    encoded_value = """
        {
            "title": "Tron: Legacy",
            "composer": "Daft Punk",
            "release_year": 2010,
            "budget": 170000000,
            "actors": null,
            "won_oscar": false
        }
    """
    tron = json.loads(encoded_value)

If you look at the result, we have a valid python dictionary with all data
properly converted, *false* is now a Python boolean and *null* is converted to
**None**:

    >>> print(tron)
    {'title': 'Tron: Legacy', 'composer': 'Daft Punk', 'release_year': 2010, 'budget': 170000000, 'actors': None, 'won_oscar': False}
    >>>


Writing JSON
############

Suppose you want to store the data about Gattaca movie in a database, or send it
to a remote user. To convert this dictionary int a valid JSON string you use the
**dumps()** method (read as *dump-s*):

    >>> print(movie)
    {'title': 'Gattaca', 'release_year': 1997, 'is_awesome': True, 'won_oscar': False, 'actors': ['Ethan Hawke', 'Uma Thurman', 'Alan Arkin', 'Loren Dean'], 'budget': None, 'credits': {'director': 'Andrew Niccol', 'writer': 'Andrew Niccol', 'composer': 'Michael Nyman', 'cinematographer': 'Slawomir Idziak'}}
    >>> json.dumps(movie)
    '{"title": "Gattaca", "release_year": 1997, "is_awesome": true, "won_oscar": false, "actors": ["Ethan Hawke", "Uma Thurman", "Alan Arkin", "Loren Dean"], "budget": null, "credits": {"director": "Andrew Niccol", "writer": "Andrew Niccol", "composer": "Michael Nyman", "cinematographer": "Slawomir Idziak"}}'
    >>>

When you call the method simply pass in the dictionary. The result is a string in
proper JSON format. Notice that *true* and *false* are both lowercase, and that
*None* was converted to *null*.

Let's now create a new object, convert it to JSON, and write it to a file. We
start by creating a dictionary. For this example, we will use data for the movie
*Minority Report*, directed by Steven Spielberg, with a soundtrack by John
Williams... This is a must-see movie for any Python programmer.

    >>> cool_movie = {}
    >>> cool_movie["title"] = "Minority Report"
    >>> cool_movie["director"] = "Steven Spielberg"
    >>> cool_movie["composer"] = "John Williams"
    >>> cool_movie["actors"] = ["Tom Cruise", "Colin Farrel", "Samantha Morton", "Max von Sydow"]
    >>> cool_movie["is_awesome"] = True
    >>> cool_movie["budget"] = 102000000
    >>> cool_movie["cinematographer"] = "Janus Kaminski"
    >>>

To write this object to a file in JSON format, we must first open a file. Next
call the **dump()** method, passing in the dictionary as the first argument and
the file second:

    >>> with open("cool_movie.json", "wt") as outfile:
    ...     json.dump(cool_movie, outfile)
    ...
    >>>

If we open the file we see that all the data is in there, everything is properly
formatted:

:: cool_movie.json

    {"title": "Minority Report", "director": "Steven Spielberg", "composer": "John Williams", "actors": ["Tom Cruise", "Colin Farrel", "Samantha Morton", "Max von Sydow"], "is_awesome": true, "budget": 102000000, "cinematographer": "Janus Kaminski"}%


Pretty printing JSON
####################

To analyze and debug JSON data, we may need to print it in a more readable
format. This can be done by passing additional parameters **indent** and
**sort_keys** to **json.dumps()** and **json.dump()** method.

.. code-block:: python

    import json

    person_string = '{"name": "Bob", "languages": "English", "numbers": [2, 1.6, null]}'

    # Getting dictionary
    person_dict = json.loads(person_string)

    # Pretty Printing JSON string back
    print(json.dumps(person_dict, indent=4, sort_keys=True))

This will make sure the output is indented and keys are ordered in ascending
order. If you do not specify any of these arguments, the default value of
**indent** is **None**, and for **sort_keys** is **False**.

.. code-block:: javascript

    {
        "languages": "English",
        "name": "Bob",
        "numbers": [
            2,
            1.6,
            null
        ]
    }

