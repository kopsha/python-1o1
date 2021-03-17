**********
Text files
**********

Files are everywhere in the digital universe. When you write a Python program,
you save your code in a file. Starting an app with your VR eye implants will
launch a cloud service that is also contained in a file. Even your operating
system consists of a mountain of files. Working with files is an essential part
of life as a software engineer. So today we will learn how to read and write
text files. And by the way, the lesson you are now reading is stored in a file.


Read
####

There are two kinds of files: text and binary. Text files are generally human
readable data, like plain text, XML, JSON or even source code. Binary files are
used for storing compiled code, app data, and media files, like images, audio
and video files.

To open a file in Python, you use the built-in **open** function. This is a
powerful and versatile function. There are `pages
<https://docs.python.org/3/library/functions.html#open>`_ of documentation on
all ways you can use this function. Today we will focus on the *file* and the
*mode*.

Begin by making a sample text file using your favourite editor. What better
example than a brief biography of Guido van Rossum, the creator of Python. This
text file will be named **guido_bio.txt**. To save time, I am pasting the text
from Guido's personal web site:

.. code-block:: text

    Guido van Rossum is the creator of the Python programming language. He grew
    up in the Netherlands and studied at the University of Amsterdam, where he
    graduated with a Master's Degree in Mathematics and Computer Science. His
    first job after college was as a programmer at CWI, where he worked on the
    ABC language, the Amoeba distributed operating system, and a variety of
    multimedia projects. During this time he created Python as side project. He
    then moved to the United States to take a job at a non-profit research lab
    in Virginia, married a Texan, worked for several other startups, and moved
    to California. In 2005 he joined Google, where he obtained the rank of Senior
    Staff Engineer, and in 2013 he started working for Dropbox as a Principal
    Engineer. In October 2019 he retired. Until 2018 he was Python's BDFL
    (Benevolent Dictator For Life), and he is still deeply involved in the
    Python community. Guido, his wife and their teenager live in Silicon Valley,
    where they love hiking, biking and birding.
    Guido's home on the web is http://www.python.org/~guido/.


Now save and let's start python and read it. One way to open a file is to call
the **open** function with the name or path to the file. Without any other
arguments, it will open the file in read mode and return a file object which we
call **file**. To read the contents of the file, call the **read()** method. This
will return all the text in the file. Finally, close the file.

    >>> file = open("guido_bio.txt")
    >>> text = file.read()
    >>> file.close()
    >>> print(text)
    Guido van Rossum is the creator of the Python programming language. He grew
    up in the Netherlands and studied at the University of Amsterdam, where he
    graduated with a Master's Degree in Mathematics and Computer Science. His
    first job after college was as a programmer at CWI, where he worked on the
    ABC language, the Amoeba distributed operating system, and a variety of
    multimedia projects. During this time he created Python as side project. He
    then moved to the United States to take a job at a non-profit research lab
    in Virginia, married a Texan, worked for several other startups, and moved
    to California. In 2005 he joined Google, where he obtained the rank of Senior
    Staff Engineer, and in 2013 he started working for Dropbox as a Principal
    Engineer. In October 2019 he retired. Until 2018 he was Python's BDFL
    (Benevolent Dictator For Life), and he is still deeply involved in the
    Python community. Guido, his wife and their teenager live in Silicon Valley,
    where they love hiking, biking and birding.
    Guido's home on the web is http://www.python.org/~guido/.
    >>>

We can print the text to see that everything worked. This method of opening,
reading and closing a file is simple. It only took three lines. But there is a
danger. What if something goes wrong before you close the file? You do not want
to litter your operating system's memory with open files. Because of this, there
is a better and safer way that is also 33% shorter. This method is to open a file
using the **with** keyword. As before, the open function will create a file
object and assign it to the name you specify. You can then read the contents
like before, but with this technique you do not need to close the file. That is
done for you. In fact, Python will close the file even if an exception occurs in
the code block. That is first class service, indeed.

    >>> with open("guido_bio.txt") as file:
    ...     contents = file.read()
    ...
    >>> print(contents)
    Guido van Rossum is the creator of the Python programming language. He grew
    up in the Netherlands and studied at the University of Amsterdam, where he
    graduated with a Master's Degree in Mathematics and Computer Science. His
    first job after college was as a programmer at CWI, where he worked on the
    ABC language, the Amoeba distributed operating system, and a variety of
    multimedia projects. During this time he created Python as side project. He
    then moved to the United States to take a job at a non-profit research lab
    in Virginia, married a Texan, worked for several other startups, and moved
    to California. In 2005 he joined Google, where he obtained the rank of Senior
    Staff Engineer, and in 2013 he started working for Dropbox as a Principal
    Engineer. In October 2019 he retired. Until 2018 he was Python's BDFL
    (Benevolent Dictator For Life), and he is still deeply involved in the
    Python community. Guido, his wife and their teenager live in Silicon Valley,
    where they love hiking, biking and birding.
    Guido's home on the web is http://www.python.org/~guido/.
    >>>

Just to be sure, print the text to check that everything worked.


But what happens if you try to open a file that does not exist? Then Python will
raise a *file not found* error. One way to handle this is to wrap the file code
in a **try** block, where we can handle a *file not found* exception. For example
if the file does not exist, you might want *text* to store the value **None**.

.. code-block:: python

    try:
        with open ("lottery_numbers.txt") as f:
            text = f.read()
    except FileNotFoundError:
        text = None

    print(text)

If you run this it displays *None*, since the file was not found. And if you
replace the file name with the one we created earlier ("guido_bio.txt"), it
successfully reads the existing file.

If you don't provide any argument to the **read()** method, it will read the
entire content of the file in memory. Typically, for text files this is the
recommended method. But if you know you need to handle huge files (larger than
your computer memory for example) you may want to read and process the text file
line by line. Luckily Python file objects already have a couple of methods,
please have a look at the official `file documentation
<https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files>`_.

For reading lines from a file, you can loop over the file object. This is memory
efficient, fast, and leads to simple code:

    >>> for line in f:
    ...     print(line, end='')
    ...
    This is the first line of the file.
    Second line of the file
    >>>

If you want to read all the lines of a file in a list you can also use the
**list()** constructor:

    >>> all_lines = list(f)
    >>>

or the **readlines()** method:

    >>> all_lines = f.readlines()
    >>>


Write
#####

Let us now see how to write a text file. For an example, we will write the names
of the five oceans to a txt file. In this case, you need an additional argument
to the **open()** function: mode **"w"** for write. If you do not specify a mode,
Python will open the file in *read mode* by default. To write the names of the
oceans to the file, loop over the list and use the **write()** method.
Remember, when using the **with** technique for opening files, Python will
automatically close the files for you.

.. code-block:: python

    oceans = ["Pacific", "Atlantic", "Indian", "Arctic", "Southern"]
    with open ("oceans.txt", "w") as f:
        for ocean in oceans:
            f.write(ocean)

Here, if the file *oceans.txt* does not exist, Python will create it. And if the
file already exists, Python will overwrite it. So be careful.

Let's open the file and see if this worked.

.. code-block:: text
    :caption: oceans.txt

    PacificAtlanticIndianArcticSouthern

While it did write the ocean name, there are no line separators. That is because
we did not write one, and Python does not assume we want them. One way to fix
this is two write a new line after writing the name of each ocean.

.. code-block:: python

    oceans = ["Pacific", "Atlantic", "Indian", "Arctic", "Southern"]
    with open ("oceans.txt", "w") as f:
        for ocean in oceans:
            f.write(ocean)
            f.write("\n")

Now, if you run the code, and then open the file, you will see each name is on
a separate line.

.. code-block:: text
    :caption: oceans.txt

    Pacific
    Atlantic
    Indian
    Arctic
    Southern


There is another way to ensure that each string is on a separate
line. You can use the **print()** function and have it to print to the file by
using the *file* keyword argument.

.. code-block:: python

    oceans = ["Pacific", "Atlantic", "Indian", "Arctic", "Southern"]
    with open ("oceans.txt", "w") as f:
        for ocean in oceans:
            print(ocean, file=f)

If you run this, and look at the file, you get the same result. Each name is on
a separate line.

.. code-block:: text
    :caption: oceans.txt

    Pacific
    Atlantic
    Indian
    Arctic
    Southern


Append
######

Notice that every time we ran our code, any text in the file was overwritten.
This is because we open the file in *write* mode. But what if you would like to
write to a file without overwriting any existing text?

For this, you open the file in *append mode* by using an **"a"** after the file
name. Append mode will create the file if it does not exist, but if the file does
exist, then Python will append your text *to the end*. It will not overwrite any
existing text.

.. code-block:: python

    oceans = ["Pacific", "Atlantic", "Indian", "Arctic", "Southern"]
    with open ("oceans.txt", "w") as f:
        for ocean in oceans:
            print(ocean, file=f)

    with open("oceans.txt", "a") as f:
        print("=======================", file=f)
        print("These are the 5 oceans.", file=f)


Let us see that this is the case.

.. code-block:: text
    :caption: oceans.txt

    Pacific
    Atlantic
    Indian
    Arctic
    Southern
    =======================
    These are the 5 oceans.

