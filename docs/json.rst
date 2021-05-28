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

Format
######

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

Notice how it looks just like a Python dictionary with a few exceptions:
* **true** and **false** are not capitalized in JSON, while in Python they are
* instead of **None** we use JavaScript value **null**

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


The JSON Module
###############

