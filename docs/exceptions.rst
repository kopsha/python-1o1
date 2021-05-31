**********
Exceptions
**********

Long before the computing era, Benjamin Franklin once said: *"If you fail to
plan, you are planning to fail."*
As you may have already noticed, when running computer programs, something
unexpected always happens. Even when they are really simple, like the ones in
these lessons: maybe a file is not there when you try to read it, or you type a
string where a number was needed or simply you press *<Enter>* when you should
have entered some text.

If there is a way for code to break, then somehow, somewhere, someone will break
it. Using *exceptions* you can manage these problems in a responsible way: if a
client asks you to capitalize an integer you can decline their bizarre
suggestion. Once you learn how to do this, you will become an exceptional Python
programmer.

An *exception* is an error that is *raised* by Python, when the execution of our
code results in an unexpected outcome. Normally, an exception will have a *type*
and a *message*. For example, when python prints such exceptions::

    ZeroDivisionError: division by zero
    TypeError: must be str, not int
    IndexError: list index out of range

The **ZeroDivisionError**, **TypeError** and **IndexError** represent the error
*type* and the text that follows the colon is the error *message*. This message
usually describes the cause of the error in more detail and/or the expected vs.
actual input.

