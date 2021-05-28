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

Load
####

Here is a typical JSON data packet.

.. code-block: json
    {
        "title": "Gatacca",
        "release_year": 1997,
    }
