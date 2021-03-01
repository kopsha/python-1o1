************
Dictionaries
************

A standard data structure in computer science is the *associative array*, which
is also called a *map*. In Python, this structure is called a *dictionary*.
Dictionaries are used when you have *key / value* pairs of data -- an input
which is mapped to an output.

Unlinke sequences, which are indexed by a range of numbers, dictionaries are
indexed by keys, which can be any immutable type (strings, numbers, booleans,
tuples). You can't use lists as keys, since lists can be modified in place.


Create
######

It is best to think of a dictionary as a set of *key*: *value* pairs, with the
requirement that the keys are unique (within on dictionary). A pair of braces
create an empty dictionary: **{}**. Placing a comma-separated list of key:value
pairs withing the braces will add initial key:value pairs to the dictionary.
This is also the way dictionaries are printed on console.

Suppose we are creating a new social network called "FriendSpace" where any life
form or intelligent agent is allowed to join. Let us make our first post to
*FriendSpace*, we will use this post to show you how to create a dictionary.

To begin, we will collect several pieces of data for each post:

    >>> # FriendSpace post
    >>> # user_id = 209
    >>> # message = "I am learning about dictionaries. Yay!"


Exercises
#########

1. Check wether an element exists within a tuple.

#. Sum up all the number elements within a tuple.

#. Find the repeated items of a tuple.

#. Print out all pair combinations of two tuples.
