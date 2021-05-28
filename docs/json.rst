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

    Yikes! That sounds pretty technical. Definitely. But in reality, all we’re
    talking about here is *reading* and *writing*. Think of it like this:
    encoding is for writing data to disk, while decoding is for reading data
    into memory.


Serializing JSON
****************

What happens after a computer processes lots of information? It needs to take a
data dump. Accordingly, the json library exposes the **dump()** method for writing
data to files. There is also a **dumps()** method (pronounced as “dump-s”) for
writing to a Python string.

Simple Python objects are translated to JSON according to a fairly intuitive
conversion:

======              ======
Python	            JSON
======              ======
dict	            object
list, tuple         array
str	                string
int, long, float	number
True	            true
False	            false
None                null


Example
*******

Here is a typical JSON data packet.

.. code-block: json
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
            "cinematographer": "Slawomir Idziak",
        }
    }

This JSON object contains examples of all possible data types. All the keys are
*strings*, but the values can be *strings*, *numbers*, *booleans*, *list*, *null*
or even another JSON object.

Now, compare it with the XML version:

.. code-block: xml
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
text of the openning tags. A popular sports is debating the merits of JSON versus
XML. But instead of arguing, I recommend you learn the pros and cons of both
formats, then choose the one which is best for your project.
