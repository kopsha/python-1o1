****************
Lambda functions
****************

In Python, a *lambda function* refers to a small, anonymous function. We call
the functions *anonymous* because technically it has no name, and we don’t define
it with the standard **def** keyword that we normally use in Python. Instead,
lambda functions are defined as one-liners that execute a single expression.

    Before we get started, a quick note: throughout this lesson I will use the
    terms *anonymous functions*, *lamda functions* or *lambda expressions*
    interchangeably. They all mean the same thing.

Although they look different, lambda functions behave in the same way as regular
functions that are declared using the *def* keyword. They are executed in a
similar way as regular Python functions, with the exception that they strictly
execute a single expression.

Lambda functions are mainly used for creating small, single-use functions. You’ll
often see them in-place of what might otherwise be a fully defined function, but
written as a lambda to save time and space.

For a concrete description, lambda functions can be understood through the
following 3 points:

- A lambda function must always execute a single expression
- An expression is a Python code run by the lambda function, which may or may
  not return any value
- A lambda function can take any number of input arguments and return any number
  of output arguments, as long as the function is maintained as a single
  expression


Definition
##########

Here is the general way to create a lambda expression: you type the keyword
``lambda`` followed by zero or more inputs, next type a ``:`` (colon), then
finally, you enter a single expression. This expression is the return value.
Just like functions, it is perfectly acceptable to have anonymous functions with
no inputs. But remember, you cannot use lambda expressions for multi-line
functions.

.. code-block:: python

    lambda arguments: expression

For example, let's say we want to declare a lambda function that computes the
remainder of a division operation. Of course, we could do this without a
function with Python’s ``%`` operator, but it’s not very readable when going
through the code. It’s easy to miss and not intuitive to catch when reading
through for the first time.

When we use a lambda function however, we’re able to clean things up for better
readability and cleaner code:

.. code-block:: python

    compute_remainder = lambda x, y: x % y

Our lambda function takes on 2 arguments, ``x`` and ``y``, and then computes the
remainder of those 2 using Python’s ``%`` operator via ``x % y``. To call the
function, all we have to do is apply it like any other regular Python function
by passing the arguments and saving the return value in a variable.

.. code-block:: python

    ### Prints out 1
    r = compute_remainder(10, 3)
    print(r)

Our code using the lambda function is simple and contained. Let us now see
another example. Suppose you are processing user data from a web registration
form, and would like to combine the first and last names into a single string
*full name* for displaying on the user interface.

We will call this lambda expression ``full_name``, which will take two arguments
*first* and *last* names, and before combining them together we will clean up
any extra whitespace characters from the names, using **strip()**, and apply the
titlecase transformation using **title()**. This is necessary because humans are
sloppy when typing.

.. code-block:: python

    full_name = lambda first, last: first.strip().title() + " " + last.strip().title()
    print(full_name("   leonhard", "EULER"))
    # Will print out: 'Leonhard Euler'

We should not judge Euler's typing skills, as this is the first time he has ever
used a computer.


Trully anonymous
################

Let us now see a common use of lambda expressions where we do not give it a name.
Suppose we have a list of science fiction authors. We would like to sort this
list by last name. Notice that some of these authors have a middle name, while
others have initials.

    >>> scifi_authors = ["Isaac Asimov", "Ray Bradbury", "Robert Heinlein", "Arthur C. Clarke", "Frank Herbert", "Orson Scott Card", "Douglas Adams", "H. G. Wells", "Leigh Brackett"]

Our strategy will be to create an anonymous function that extracts the last name
and uses that as the sorting criteria.

    To access the last name, split the string into pieces wherever it has a
    space.

    Next, access the last piece by index **-1**

    And, as a final precaution, convert the string to lowercase. This way the
    sorting is not case-sensitive. Trust me, some people do not know how to use
    the shift key.


    >>> ordered_authors = sorted(scifi_authors, key=lambda name: name.split(" ")[-1].lower())
    >>> print(ordered_authors)
    ['Douglas Adams', 'Isaac Asimov', 'Leigh Brackett', 'Ray Bradbury', 'Orson Scott Card', 'Arthur C. Clarke', 'Robert Heinlein', 'Frank Herbert', 'H. G. Wells']
    >>>

The list is now in alphabetical order. These names are a pleasure to read.


Higher order functions
######################

We must go deeper. The power of lambda is better shown when we define a function
that makes functions. Say you have a function definition that takes one argument,
and that argument will be multiplied with an unknown number:

.. code-block:: python

    def create_multiplier_function(n):
        return lambda x: x * n

Use that function definition to make a function that always *doubles* the number
you send in. Or, use the same function definition to make a function that always
*triples* the number you send in

    >>> my_doubler = create_multiplier_function(2)
    >>> print(my_doubler(11))
    22
    >>> my_tripler = create_multiplier_function(3)
    >>> print(my_tripler(11))
    33
    >>>

Suppose you are working with quadratic functions. Perhaps you are computing the
trajectories of cannonballs. To do this, let's write a function called
**make_quadratic_function**, and its inputs are the three coefficients **a**,
**b** and **c**:

.. code-block:: python

    def make_quadratic_function(a, b, c):
        """Creates a function f(x) = ax^2 + bx + c"""
        return lambda x: a*x**2 + b*x + c

And use this function definition to create a function that always doubles the
number you send in:

Let's test this by creating the function :math:`2x^2 + 3x - 5`

    >>> f = make_quadratic_function(2, 3, -5)
    >>> f(0)
    -5
    >>> f(1)
    0
    >>> f(2)
    9
    >>>

You can see this function works correctly.

Lambda expressions are quite useful when you need a short, throwaway function.
Something simple that you will only use once. Common applications are sorting
and filtering data.
