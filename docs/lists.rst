*****
Lists
*****

Order... matters. And python lists make it easy to work with ordered data. Lists
are a builtin data structure for storing and accessing objects which belong in
a specific sequence. We will now learn how to create and use lists, and we will
do so in a linear and orderly fashion.

- create simple lists
- lists can hold any kind of values (even other lists)
- accessing list contents by index
- slicing lists
- adding, removing items to lists
- finding items in lists
- walking through lists
- ordering items in a list
- lists comprehension


Simple uses
###########

There are two ways to create a list. One way is to use the ``list()``
*constructor*. But a simpler and more common way is to use *brackets*.

.. code-block:: python

    samples = list()
    # or ...
    samples = []


When creating a list, you can also pre-populate it with values. For example,
let's create a list with the first few prime numbers:

.. code-block:: python

    prime_numbers = [2, 3, 5, 7, 11, 13]


If you feel that these numbers are not enough, you can always add values later
by using the ``append()`` method which allows you to add new values *to the end*
of the list. Let's append the next two prime numbers: 17 and 19.

.. code-block:: python

    prime_numbers.append(17)
    prime_numbers.append(19)

    print(prime_numbers)


If you display the list, you will see it contains the new values.
Notice how lists preserve the order of the data; this is different from sets.
In sets, the order is not important. In lists order is everything.

You do not have to view the entire list. If you want to see a specific value,
you can access it by its index.

.. note ::

    In computer science, we start counting indexes with 0, not 1. So in our
    list *prime numbers* are indexed 0, 1, 2, 3...


.. code-block:: python

    [ 2,  3,  5,  7, 11, 13, 17, 19 ]
      ^
      0   1   2   3   4   5   6   7


To view the first item, you type the name of the list and the index in
brackets. The first item is 2. The second item has index 1 and the second
item is 3. And so on.

.. code-block:: console

    >>> primes
    [2, 3, 5, 7, 11, 13, 17, 19]
    >>> primes[0]
    2
    >>> primes[1]
    3
    >>> primes[2]
    5


Notice how the indexes increase by one as you go from left to right. And they
decrease by one as you go from right to left. When you get to the beginning the
index is 0. If you decrease the index once more, you get -1. Here, Python wraps
back around to the end of the list. So the last item has the index -1, the next
to last -2, and so on.

.. code-block:: console

    >>> primes
    [2, 3, 5, 7, 11, 13, 17, 19]
    >>> primes[-1]
    19
    >>> primes[-2]
    17
    >>> primes[-8]
    2


This is convenient when you want to look at the values at the end of a list.
The last item is 19, the next to last prime is 17. And so on, until we reach
the beginning of the list with index -8. Be careful, you can only wrap around once. If you try to find the value of index -9, you get an index error.

.. code-block:: console

    >>> primes
    [2, 3, 5, 7, 11, 13, 17, 19]
    >>> primes[-9]
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    IndexError: list index out of range


Slicing
#######

Another way to access values in a list is by slicing. This let's you retrieve a
range of values from your list. We will continue to use our lists of primes. To
slice this list, type the name of the list, bracket, *a starting index*, a
colon, *a stopping index*, then a closing bracket.

.. code-block:: console

    >>> primes
    [2, 3, 5, 7, 11, 13, 17, 19]
    >>> primes[2:5]
    [5, 7, 11]


The result is a sublist that starts at index 2, and continues until it reaches
index 5. Be careful, slicing includes the value at the starting index, but
excludes the stopping index. The beginning value is included, the ending value is not.

One more slice...

.. code-block:: console

    >>> primes
    [2, 3, 5, 7, 11, 13, 17, 19]
    >>> primes[0:6]
    [2, 3, 5, 7, 11, 13]


This will start at the beginning, which is index 0, and continue to index 6,
which is 17. It will not include the final number, so this slice includes the
primes from 2 through 13, in other words: the first 5 values.

Notice, that if you start from the beginning, you can ommit the 0 completely
and the slice will assume that you want to start from index 0. Similarly, if
you omit the stopping index it will assume that you want to go the end of the
list.

.. code-block:: console

    >>> primes
    [2, 3, 5, 7, 11, 13, 17, 19]
    >>> primes[:6]
    [2, 3, 5, 7, 11, 13]
    >>> primes[6:]
    [17, 19]


Multiple data types
###################

Lists can contain more than prime numbers. They can contain integers, booleans,
strings, floats, and even other lists.

.. code-block:: python

    examples = [128, True, "Alphabet", 3.14, [32, 64, False]]
    print(examples)


Many languages require lists to contain values of the same type, but not
Python. With Python you are free to insert multiple data types in the same
list. Lists can also contain duplicate values. Here is another way lists
are different from sets. For example, suppose you want to record the
numbers you roll on a pair of dice. Pretent you roll a 4, 7, 2, 7, 12, 4 and 7.

.. code-block:: console

    >>> rolls = [4, 7, 2, 7, 12, 4, 7]
    >>> rolls
    [4, 7, 2, 7, 12, 4, 7]


If you look at the list, all the values are there, even the repeated rolls. You
can also combine lists. To see how, create two separate lists: a list of
numbers and a list of letters... To combine these two lists into a single list
use the plus sign.

.. code-block:: console

    >>> numbers = [1, 2, 3]
    >>> letters = ["a", "b", "c"]
    >>> numbers + letters
    [1, 2, 3, 'a', 'b', 'c']


But order matters, if you reverse this and compute ``letters + numbers`` you
get ``'a', 'b', 'c', 1, 2, 3``. Combining lists is called concatenation.
Observe. The list of numbers and the list of letters are unchanged.

.. code-block:: console

    >>> letters + numbers
    ['a', 'b', 'c', 1, 2, 3]
    >>> numbers
    [1, 2, 3]
    >>> letters
    ['a', 'b', 'c']


There are many other methods for working with lists. To see them all, pass any list to the directory function. To learn how to use one of these methods, use the help function. For example, there is a method for reversing the list. The
help text gives full details on what it does and how to use it.

.. code-block:: console

    >>> dir(numbers)
    ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
    >>> help(numbers.reverse)
    Help on built-in function reverse:

    reverse() method of builtins.list instance
        Reverse *IN PLACE*.


For now, you can ignore the methods starting with double underscores. Feel free
to try them out.


Lists comprehension
###################

When coding you spend a lot of time making lists, in many languages this can be
tedious: create an empty list, set up a for loop, then add the items to the
list one by one. Python cares about your sanity and gives you a tool to
simplify this process: *list comprehension*. In most cases let you construct
a new list in a single line of code. It's now time for Python to shine and
save time with a single line.

We will cover many examples of lists comprehensions, but first let's talk about
them generally. In Python lists are a collection of data surounded by brckets
and the elements are separated by commas. A list comprehension is also
surounded by brackets but instead of a list of data inside you enter an
expression followed by for loops and if clauses. Here is the most basic form
for a list comprehension:

    [ *expr* for *value* in *collection*]

The first *expression* generates the elements in the list and you follow this
with a for loop over some *collection* of data. This will evaluate the
expression for every item in the collection. If you want to include the
expression for certain pieces of data you can add on an if clause after the
for loop. The expression will be added to the list only if clause its true.

    [ *expr* for *value* in *collection* if *condition*]

You can even have more than one if clause and the expression will be added
to the list only if all the clauses are true.

    [ *expr* for *value* in *collection* if *condition1* and *condition2*]

And you can even loop over more than one collection.

    [ *expr* for *val1* in *collection1* for *val2* in *collection2*]

Let's now see some examples. For our first example, let's create a list of the
squares of the first 10 pozitive integers. Let's first do this without list
comprehensions.

To begin you might create an empty list called ``squares``, next you would loop
over the first 10 positive integers. You would then append the square of each
to the list of squares.

.. code-block:: python

    squares = []
    for i in range(1, 11):
        squares.append(i**2)
    print(squares)

    # this is the output
    [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


Notice that an exponent in Python is represented by double asterisks. Why oh why
do they not used the intergalactic mathematical notation for exponents ? To see
that this works print list *squares*.

Let's do this once more using list comprehensions:

    squares2 = [i**2 for i in range(1,11)]

If you print this, you get the exact same list, but we only needed one line of
code instead of three. Let's now look at a slightly more complex example. We'll
create a list of remainders when you divide the first 10 squares by 5.

    To find the remainder when you divide by 5 use the ``%`` operator.

.. code-block:: python

    remainders = [ (x ** 2) % 5 for x in range(1,11) ]
    print(remainders)

    # this is the output
    [1, 4, 4, 1, 0, 1, 4, 4, 1, 0]

If you print the list, you'll see that there are only three perfect squares mod
5: 0, 1 and 4. This example shows you that the expressions in the list
comprehensions can be complex. By the way, if you look at the remainders when
you divide by a prime number *p* you'll notice an interesting pattern: the
number of remainders is (p+1)/2. The problem of finding which number appear in
the list is a comple puzzle from number theory known as *quadratic reciprocity*
and was first proved by Gauss.

Next, let's create a list comprehension that has an if clause. Suppose we have
a list of movies and we want to find those movies that start with the letter G.
Let's see how to do this with and without lists comprehensions.

If you're not using list comprehensions you'd start by making an empty list, next
loop over the list of movies. We can use the ``startswith()`` method to see if
the title starts with the letter G. If it does, then append it to out list.

.. code-block:: python

    movies = [
        "Star Wars", "Ghandi", "Casablanca", "Shawshank Redemption",
        "Toy Story", "Gone with the wind", "Citizen Kane", "It's a wonderful life",
        "The Wizard of Oz", "Gattaca", "Rear Window", "Ghostbusters",
        "To Kill a Mockingbird", "Good Will Hunting", "2001: A Space Odissey",
        "Riders of the Lost Ark", "Groundhog Day",
        "Close Encounters of the Third King", "Scent of a Woman",
    ]

    g_movies = []
    for title in movies:
        if title.startswith("G"):
            g_movies.append(title)


Print the list to make sure that it worked. But this four line routine can be
done in a single line with a list comprehension. The expression we want to
appear in our list is simply the title, next loop over the movies, but also
check that the title starts with the letter G.

.. code-block:: python

    g_movies = [title for title in movies if title.startswith("G")]


Print and observe: we get the same answer with a single line of code.

    ["Ghandi", "Gone with the wind", "Gattaca", "Ghostbusters", "Good Will Hunting", "Groundhog Day"]

Let's complicate this example a bit more. Suppose our list of movies is a list
of tuples containing both the title of the movie and the year it was released.
What if we want a list of titles of all movies that were released before the year
2000. How would you do this using lists comprehensions.

As before we want our list to only contain the titles, but this time when we
write the *for-loop* each element is a tuple. Next we select the movies released
before 2000 using an *if* clause on the year.

.. code-block:: python

    movies = [
        ("Citizen Kane", 1941), ("Spirited Away", 2001),
        ("It's a wonderful life", 1946), ("Gattaca", 1997),
        ("No Country for Old Men", 2007), ("Rear Window", 1954),
        ("The Lord of the Rings: The Fellowship of the Ring", 2001),
        ("Groundhog Day", 1993), ("Close Encounters of the Third King", 1977),
        ("The Aviator", 2004), ("Riders of the Lost Ark", 1981),
    ]

    pre2k = [title for title, year in movies if year < 2000]

If you print the list, you can see that it worked. In this example the if clause
used the *year* but the *year* was not included in the list, only the title is
included.

Let's see a mathematical example, suppose you use a list to represent a vector,
how would you perform scalar multiplication on this vector?

    ``v = [2, -3, 1]``

That is what if we want to multiply each number by 4. You might be tempted to
try ``4 * v`` but look what happens, this is unusual:

.. code-block:: console

    >>> v = [2, -3, 1]
    >>> 4 * v
    [2, -3, 1, 2, -3, 1, 2, -3, 1, 2, -3, 1]


What happened here is **4** times **v** is the same as **v + v + v + v** and in
Python if you add two lists it concatenates them rather than adding them
component wise. For example if you add ``[2, 4, 6]`` and ``[1, 3]`` you get the
list ``[2, 4, 6, 1, 3]``, so ``4 * v`` is just a list containing 4 copies of
``v``. This is not what we want. We can achieve scalar multiplication with a list
comprehension where we multiply each component by 4.

.. code-block:: python

    v = [2, -3, 1]
    result = [4 * x for x in v]

If you print this vector you can see we get the desired result.


For our final example let's use list comprehensions to compute the cartesian
product of sets. The cartesian product is named after the French scholar Rene
Descartes. Recall that if you have two sets A and B is the set of pairs where the
first component is in A and the second component is in B.

.. math::

    A × B  = { (a, b) | a ∈ A, b ∈ B }

For example if **A = {1, 3}** and **B = {x, y}** then

.. math::

    A × B  = { (1, x), (1, y), (3, x), (3, y) }

Now let's compute the cartesian product of two sets in Python using lists
comprehensions.

.. code-block::

    A = [1, 3, 5, 7]
    B = [2, 4, 6, 8]

    cartesian_product = [(a, b) for a in A for b in B]


If you print the product, you can see the list contains all 16 possible pairs.
Using this technique you can even compute the cartesian product of three or more
sets.


.. note ::

    Lists start at 0 and they end precisely when you are finished. You can
    slice them, you can concatenate them, you can reverse them, you can sort
    them, *comprehend* them. You can even clear them.

    If I were to make a list of all uses of lists, I would have a very, VERY
    long list.

