************
Dictionaries
************

A standard data structure in computer science is the *associative array*, which
is also called a *map*. In Python, this structure is called a *dictionary*.
Dictionaries are used when you have *key-value* pairs of data -- an input
which is mapped to an output, with the requirement that the keys are unique
(within the same dictionary of course).

Unlike sequences, which are indexed by a range of numbers, dictionaries are
indexed by keys, which can be any immutable type (strings, numbers, booleans,
tuples). You can't use lists as keys, since lists can be modified in place.


Create
######

Suppose we are creating a new social network called "FriendSpace" where any life
form or intelligent agent is allowed to join. Let us make our first post to
*FriendSpace*, we will use this post to show you how to create a dictionary.

To begin, we will collect several pieces of data for each post:

    >>> # FriendSpace post
    >>> # user_id = 209
    >>> # message = "I am learning about dictionaries. Yay!"
    >>> # language = "English"
    >>> # created = "2021-03-02T10:11:06.278326"
    >>> # location = (46.766667, 23.583333)
    >>>

Using dictionaries we can store all of this data in a single object. A pair of
braces create an empty dictionary:

    >>> empty_dictionary = {}
    >>>

Placing a comma-separated list of key-value pairs withing the braces will add
initial key-value pairs to the dictionary. This is also the way dictionaries are printed on console.

    >>> post = {"user_id": 209, "message": "I am learning about dictionaries. Yay!", "language": "English", "created": "2021-03-02T10:11:06.278326", "location": (46.766667, 23.583333)}
    >>>

We have created a dictionary called **post** with 5 pieces of data. If you think
of a dictionary as a map, there are 5 inputs and 5 outputs. In Python, these
inputs are called *keys*, and the outputs are called *values*.

.. table:: post dictionary
    :widths: auto

    ==========  ===========
     Keys        Values
    ==========  ===========
     user_id     209
     message     "I am learning about dictionaries. Yay!"
     language    "English"
     created     "2021-03-02T10:11:06.278326"
     location    (46.766667, 23.583333)
    ==========  ===========

Notice how the values have a variety of data types in this dictionary: an
integer, three strings and a tuple of floats. Python is flexible: you can use
all kinds of data types for both keys and values. You are free to mix and match
data to suit your needs.

    >>> type(post)
    <class 'dict'>
    >>>


If you use the *type* function, you will see *post* is an instance of the *dict*
class. This suggests we can use the **dict** constructor to create a dictionary.
Let's create another *FriendSpace* post using the dict constructor. This time,
we will only provide a few pieces of data...

    >>> post2 = dict(message="There is always another way.", language="English")
    >>> print(post2)
    {'message': 'There is always another way.', 'language': 'English'}
    >>>

You can see this made a dictionary. We add additional pieces of data by using
brackets. The key name goes inside the brackets, and you use the equals sign to
assign the value.

    >>> post2["user_id"] = 209
    >>> post2["created"] = "2021-03-02T10:11:06.278326"
    >>> print(post2)
    {'message': 'There is always another way.', 'language': 'English', 'user_id': 209, 'created': '2021-03-02T10:11:06.278326'}
    >>>

Notice that in the constructor, you did not have to put quotes
around the keyname, but when you add new data using brackets, you do use quotes.
If you print the dictionary, you will see all the data is there inside braces.


Access data
###########

Just as you use brackets to store new data in a dictionary, you use brackets to
access data as well. For example, to see the message from the first post, use
the key name "message" inside brackets.

    >>> print(post["message"])
    I am learning about dictionaries. Yay!
    >>>

But do not be careless. Let's see what happens if you try to access data that is
not in the dictionary.

    >>> print(post2["location"])
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    KeyError: 'location'
    >>>

When we created **post2**, we did not assign a location. If we try to access
this value, we get a *KeyError*. How do we avoid such catastrophe? Simple. One
way is to use the **in** operator to first check if a key is in the dictionary.

    >>> if "location" in post2:
    ...     print(post2["location"])
    ... else:
    ...     print("The post does not have a location")
    ...
    The post does not have a location
    >>>

Another way to access data in a dictionary and handle the possibility it does
not have a certain key is the *get* method. This lets you try and get the value
for a specific key. If the dictionary does not contain data for that key, you
can specify a default value. For our case let's return an empty tuple.

    >>> loc = post2.get("location", tuple())
    >>> print(loc)
    ()
    >>>

If you print the value you see the *get* method did returned an empty tuple.

Now, turn your attention back to the original post.

    >>> print(post)
    {'user_id': 209, 'message': 'I am learning about dictionaries. Yay!', 'language': 'English', 'created': '2021-03-02T10:11:06.278326', 'location': (46.766667, 23.583333)}
    >>>

A common task is to iterate over all the key value pairs in a dictionary. A
straightforward way to do this is to loop over all the keys, then get the value:

    >>> for key in post:
    ...     value = post[key]
    ...     print(key, "=", value)
    ...
    user_id = 209
    message = I am learning about dictionaries. Yay!
    language = English
    created = 2021-03-02T10:11:06.278326
    location = (46.766667, 23.583333)
    >>>

When you simply loop over a dictionary, this will give you all the keys for that
dictionary. The order of the data may be different for you. Do no panic.
Dictionaries are not ordered data. As long as you see all the data, everything
is under control.

Another way to iterate over all the key value pairs in a dictionary is to use
the **items** method. This will give you both the key and the value in each step
of the iteration.

    >>> for key, value in post.items():
    ...     print(key, "=", value)
    ...
    user_id = 209
    message = I am learning about dictionaries. Yay!
    language = English
    created = 2021-03-02T10:11:06.278326
    location = (46.766667, 23.583333)
    >>>


There are a variety of methods for working with a dictionary. The **pop** and
**popitem** methods allow you to remove a single item from a dictionary,
while the **clear** method will remove all data. To complete this lesson please
take a moment to explore and experiment with
`these methods <https://www.w3schools.com/python/python_ref_dictionary.asp>`_.


Exercises
#########

1. Create a dictionary out of the lists below:

    .. code-block:: python

        keys = ["name", "phone", "email"]
        values = ["Mike", "+40791882123", "michael@yahoo.com"]

        # Expected output
        {'name': 'Mike', 'phone': '+40791882123', 'email': 'michael@yahoo.com'}

#. Given a dictionary describing a car attributes, print the model and the year
   of the car or the string **N/A** if the value is not present.

    .. code-block:: python

        car = {
            "brand": "Ford",
            "model": "Mustang",
            "year": 1964
        }

#. Print all the key value pairs of any dictionary, but make sure they are shown
   in the same order every time (order the keys alphabetically).

#. Count the frequency of all words in the given text:

    .. code-block:: python

        text = "He ordered his regular breakfast. Two eggs sunnyside up, hash browns, and two strips of bacon. He continued to look at the menu wondering if this would be the day he added something new. This was also part of the routine. A few seconds of hesitation to see if something else would be added to the order before demuring and saying that would be all. It was the same exact meal that he had ordered every day for the past two years."

        # expected output
        {'the': 6, 'he': 4, 'two': 3, 'of': 3, 'to': 3, 'would': 3, 'be': 3, 'ordered': 2, 'and': 2, 'if': 2, 'this': 2, 'day': 2, 'added': 2, 'something': 2, 'was': 2, 'that': 2, 'his': 1, 'regular': 1, 'breakfast': 1, 'eggs': 1, 'sunnyside': 1, 'up': 1, 'hash': 1, 'browns': 1, 'strips': 1, 'bacon': 1, 'continued': 1, 'look': 1, 'at': 1, 'menu': 1, 'wondering': 1, 'new': 1, 'also': 1, 'part': 1, 'routine': 1, 'a': 1, 'few': 1, 'seconds': 1, 'hesitation': 1, 'see': 1, 'else': 1, 'order': 1, 'before': 1, 'demuring': 1, 'saying': 1, 'all': 1, 'it': 1, 'same': 1, 'exact': 1, 'meal': 1, 'had': 1, 'every': 1, 'for': 1, 'past': 1, 'years': 1}
