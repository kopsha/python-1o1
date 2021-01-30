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

Lists can contain more than prime numbers. The can contain integers, booleans,
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


For now, you can ignore the methods starting with double underscores.

.. note ::

    Lists start at 0 and they end precisely when you are finished. You can
    slice them, you can concatenate them, you can reverse them. You can even
    clear them. If I were to make a list of all uses of lists, I would have
    a very, VERY long list.


