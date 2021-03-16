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
text file will be named ``guido_bio.txt``. To save time, I am pasting the text
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
call **file**. To read the contents of the file, call the **read** method. This
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
object and assign it to the name you specify.
