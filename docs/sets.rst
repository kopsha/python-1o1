****
Sets
****

Python comes equipped with different objects to help organize your data. These
data structures include lists, tuples, sets and dictionaries. But right now,
we'll focus on sets.


Sets are useful when you are working with data and the order or frequency of the
values does not matter. Get ready to become an element of the set of people who
understand sets.


Create
######

We will begin by creating an empty set.

.. code-block:: python

    example = set()


Now we want to add things to our set, and the ``add()`` function does exactly
what we expect. Duplicates are not stored: if you try to add the same item
twice, the set will store it the first time and ignore it the second time. We
will use this method to add several objects to this set.

.. code-block:: python

    example.add(42)
    example.add(False)
    example.add(3.141592653589793)
    example.add("Thorium")


Notice that you can add data of different types to the same set. If you print
the example set we just prepared, Python will show you the items inside the set.
Each item inside a set is called an "element".

.. code-block:: python

    print(example)
    # Output
    {False, 42, 3.141592653589793, 'Thorium'}


When you try this, the elements may appear in a different order for you than
what is displayed here. Do not panic. For sets, the order does not matter. This
is different for lists and tuples where the order does matter.


Now look what happens when you try to add the number **42** to the set a second
time.

.. code-block:: python

    example.add(42)
    print(example)
    # Output
    {False, 42, 3.141592653589793, 'Thorium'}


The set still contains just one copy of the number **42**. Sets do not contain
duplicate elements. To see the number of elements in a set, use the length
function, which is shortened to : **len(example)**.


There is a second way to create a set, which can be faster in some instances.
When creating the set you can pre-populate the set with a collection of elements.


.. code-block:: python

    example2 = set([False, 42, 3.141592653589793, 'Thorium'])
    print(example2)
    # Output
    {False, 42, 3.141592653589793, 'Thorium'}


Remove
######

To remove an element from this set, use the **remove** method. Beware, if you
attempt to remove an element that is not in the set you will get an error. To
test this method, let's remove the number **42**.


.. code-block:: python

    example.remove(42)
    print(len(example))
    print(example)
    # Output
    3
    {False, 3.141592653589793, 'Thorium'}


We can check that it worked either by looking at the number of elements or
displaying all the elements inside the set. Look what happens if we try to
remove the number **50** which is not in the set:

.. code-block:: python

    example.remove(50)
    # Output
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    KeyError: 50


To avoid the possibility of an error, there is a second way to remove an element:
the **discard** method. With the *discard* method, if you try to remove an
element which is not in the set, the method does nothing -- it quietly returns
without making a change. Watch what happens when we discard the integer **50**,
which is not in the set.

.. code-block:: console

    >>> example.discard(50)
    >>>


Nothing... Peace and quiet. The choice is yours; if you want to be alerted when
your code tries to remove an element not in the set, use **remove()**.
Otherwise, discard provides a convenient alternative.


There is also a faster way to remove elements. To empty out the set and remove
all elements, use the **clear()** method.

.. code-block:: console

    >>> print(example)
    {False, 3.141592653589793, 'Thorium'}
    >>> example.clear()
    >>> len(example)
    0


This set now contains no elements -- it has become the empty set. We can move
along; there is nothing to see here.


Union and intersection
######################

Now that we know how to create and modity a set, let's learn how to evaluate the
union and intersection of two sets. If you have two sets **A** and **B**, then
the union is the combination of all elements from the two sets and in math is
denoted as :math:`A \bigcup B`.
The intersection is the set of elements inside both A and B, and is denoted as
:math:`A \bigcap B`.


To see these in action, let's look at the integers from 1 through 10.

.. code-block:: python

    odds = set([1, 3, 5, 7, 9])
    evens = set([2, 4, 6, 8, 10])
    primes = set([2, 3, 5, 7])
    composites = set([4, 6, 8, 9, 10])


The union of the odd and even integers are all numbers from 1 to 10. You get the
same answer if you reverse everything.

.. code-block:: console

    >>> odds.union(evens)
    {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    >>> evens.union(odds)
    {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

    >>> odds
    {1, 3, 5, 7, 9}
    >>> evens
    {2, 4, 6, 8, 10}


Notice how the set of *odds* and the set of *evens* are unchanged. We can find
the set of odd prime numbers by computing the intersection of the sets of
**odds** and **primes**.

.. code-block:: console

    >>> odds.intersection(primes)
    {3, 5, 7}
    >>> primes.intersection(evens)
    {2}


And there is only one even prime number: **2**.

Which integers are both *even* and *odd* ?

.. code-block:: console

    >>> evens.intersection(odds)
    set()


There are none. The intersection of these two sets is the empty set.

.. code-block:: console

    >>> primes.union(composites)
    {2, 3, 4, 5, 6, 7, 8, 9, 10}


The union of the prime numbers and composite numbers are the integers from **2**
through **10**. Notice 1 is missing -- this is becausse 1 is neither prime nor
composite.


Membership
##########


Another common opreation is testing to see if one element is inside a set. To do
this in Python use the **in** operator. Is 2 in the set of prime numbers ?


.. code-block:: console

    >>> 2 in primes
    True


Yes. This is a true statement.

Is 6 an odd integer?

.. code-block:: console

    >>> 6 in odds
    False


No. This is a false statement. You can also test to see if an element is NOT in
a set.

.. code-block:: console

    >>> 9 not in evens
    True


9 is *not* an even integer, so this is a true statement.

There are many more methods and operations you can perform with sets. Take a
moment to explore
`these methods <https://www.w3schools.com/python/python_ref_set.asp>`_.
You will not regret it.


Sets are a built-in data type in Python. They come equipped with all the luxury
features: unions, intersections, adding elements, removing elements, and much
more. Everything you will ever need for your data hungry code... Provided your
sets are *finite*.


Exercises
#########


1. Add a list of elements to a given set.

    .. code-block:: python

        given = {"Yellow", "Orange", "Black"}
        some_items = ["Blue", "Green", "Red"]
        expected = {"Green", "Yellow", "Black", "Orange", "Red", "Blue"}

#. Create a new set with all items from both sets by removing duplicates

    .. code-block:: python

        given_a = {10, 20, 30, 40, 50}
        given_b = {30, 40, 50, 60, 70}
        expected = {70, 40, 10, 50, 20, 60, 30}

#. Remove 10, 20, 30 elements from the following set

    .. code-block:: python

        given_a = {10, 20, 30, 40, 50}
        expected = {40, 50}

#. Determine wether or not the following two sets have any elements in common

    .. code-block:: python

        given_a = {10, 20, 30, 40, 50}
        given_b = {60, 70, 80, 90, 10}
        # Expected output:
        The two sets have items in common.
        {10}

#. Count the number of vowels in a given string

    .. code-block:: python

        given = "Understanding sets is easy."
        # Expected output
        The given string has 7 vowels.

