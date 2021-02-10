******
Tuples
******

Not all data can be stored in a pile, oftentime data must be ordered in a
sequence to be useful. Python offers several ways to store and work with
ordered data. *Lists* are the most common tool, but there is a smaller, faster
alternative the *tuple*.


Comparison to lists
###################

What is the difference between **lists** and **tuples**?

The quick explanation is that a list contains a sequence of data surrounded by
brackets, while the tuple contains a sequence of data surrounded by parentheses.

.. code-block:: python

    # List example
    prime_numbers = [2, 3, 5, 7, 11, 13, 17]

    # Tuple example
    perfect_squares = (1, 4, 9, 16, 25, 36)

    # Display lengths
    print("# Primes:  ", len(prime_numbers))
    print("# Squares: ", len(perfect_squares))

    # Iterate over both sequences
    for p in prime_numbers:
        print("Prime: ", p)
    for n in perfect_squares:
        print("Square: ", n)


Other than notation there seems to be little differenceb between these two. In
both cases you can use the **len()** function to display the number of elements
in the sequence, or you can iterate over the sequences and get identical
behavior.

So how are lists and tuples different from one another?
To see the difference let's have a look at the methods available to the
`lists <https://www.w3schools.com/python/python_ref_list.asp>`_. Then, let's
look at the methods available to the
`tuples <https://www.w3schools.com/python/python_ref_tuple.asp>`_.
Notice that lists have more methods available than tuples. This extra
functionality comes at a price: lists occupy more memory than tuples. When you
are working with big data sets this can be significant.

Another difference between lists and tuples is that you can add, remove or
change data in lists. Tuples cannot be changed. We say they are **immutable**.
Once you make a tuple, it is set in stone. Knowing that tuples cannot change,
enables Python to make significant optimizations.

For example, tuples can be made more quickly than lists.


Create
######

Tuples use parentheses. To make an empty tuple you simply type a pair of
parentheses. Let's quickly make a few test tuples.

.. code-block:: python

    empty_tuple = ()
    test1 = ("a")
    test2 = ("a", "b")
    test3 = ("a", "b", "c")


Next, let's print these four tuples:

.. code-block:: python

    print(empty_tuple)
    print(test1)
    print(test2)
    print(test3)

    # Output
    ()
    a        # <-- wait, what's this ?
    ('a', 'b')
    ('a', 'b', 'c')

Notice that the tuple containing a single element looks different from the
others. It looks like a string and not a tuple. To make a tuple with just one
element you need to type a comma at the end. Let's make a change and re-run.

.. code-block:: python

    empty_tuple = ()
    test1 = ("a",)
    test2 = ("a", "b")
    test3 = ("a", "b", "c")

    print(empty_tuple)
    print(test1)
    print(test2)
    print(test3)

    # Output
    ()
    ('a',)
    ('a', 'b')
    ('a', 'b', 'c')


Everything is now a tuple.

Before we explain the mistery behind the tuple with one element, let's see
another way to make a tuple. If you want, you can leave out the parentheses
altogether. Like before, to make a tuple with one element you need to end with
a comma.

.. code-block:: python

    test1 = "a",
    test2 = "a", "b"
    test3 = "a", "b", "c"

    print(test1)
    print(test2)
    print(test3)

    print(type(test1))
    print(type(test2))
    print(type(test3))


If we print each item and its type we see that all three tests are in fact
tuples.


Tuple unpacking
###############

Let's now examine the eccentric behavior of tuples with one element.
The reason for this is a feature called *tuple unpacking*.

Suppose you are working with a large dataset containing three pieces of data
about each person. Their **age**, **country** and wheter or not they
**know_python**. Perhaps this data was collected in a survey to study the
popularity of Python. We will store the results for each person in a tuple. Here
is the information from a single person from the survey.

.. code-block:: python

    # (age, country, knows_python)
    survey = (27, "Romania", True)

To access the data it is tempting to extract each piece of data individually, as
with lists, you can access elements by index. We will print the values to make
sure this method is successful.

.. code-block:: python

    age = survey[0]
    country = survey[1]
    knows_python = survey[2]

    print("Age: ", age)
    print("Country: ", country)
    print("Knows Python: ", knows_python)

This works, but tuples provide a faster alternative. Consider a second survey.
You can assign all elements in a tuple to different variables in a single line.

.. code-block:: python

    survey2 = (31, "Switzerland", False)
    age, country, knows_python = survey2

This will assign the first element to *age*, second to *country*, and third to
*knows_python*. Python unpacks all the values and assigns them for you. Please
print each value to confirm this works.

Tuple unpacking explains the need for a trailing comma when making tuples with
a single element.

.. code-block:: python

    country = ("Greece")

According to the rules of tuple unpacking this would assign the string "Greece"
to the variable **country**. By adding an extra comma at the end you are telling
Python that here you do in fact want **country** to be a tuple and you do not
want to unpack the values into the variable.

Please make sure that the number of variables matches the number of elements in
the tuple. We will look at two cases.

.. code-block:: python

    a, b, c = (1, 2, 3, 4)

Here we do not have enough variables to hold all the values in the tuple.
Running this causes a *value error*. Similarly if you have more variables than
elements in the tuple Python will raise a *value error*.

.. code-block:: python

    x, y, z = (1, 2)

There is no room for sloppy behavior when we're working with typles.

If you know a student who is reluctant to use this data structure please show
them this lesson, it will cure them of their pupil tuple scruples.


Exercises
#########

1. Check wether an element exists within a tuple.

#. Sum up all the number elements within a tuple.

#. Find the repeated items of a tuple.

#. Print out all pair combinations of two tuples.

