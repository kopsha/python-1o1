
# Basics of Structured Programming

## Understanding the Programming Pyramid

Imagine a pyramid that helps us understand how computers work. At the top, we
have what you see and use every day on your computer or phone. As we move down,
things get more technical, ending with the nuts and bolts of the computer that
make everything run.

![Computer programming pyramid](./programming-pyramid.svg)


## Programming Building Blocks

> Think of a computer as a very smart calculator that can do more than just add
> or subtract numbers.
> It can also remember things!

When we give data to computers, they help us make sense of it. Let's say you
have a list of who owes you virtual money (crypto?):
- The list has names and amounts (like a fancy checklist).
- It tells you who has paid and who hasn’t.

Here’s what a computer program composed of:
1. **Data** - This is the information, like the names and amounts.
2. **Behavior** - This is what the computer does with the data. For example:
    ```python
    if someone_has_paid:
        say_thank_you()
    ```

## Storing Data

### Basic Data Types:
- **None** - When there’s nothing there (like an empty box).
- **Numeric** - Just like the numbers you use every day.
  - _Whole numbers_: 1, 21, 35, 199, ...
  - _Decimal numbers_: 0.01, 2.3, 3.1415, ...
  - _Complex numbers_: these are a special type of number that expand upon the
    familiar real numbers used in everyday math. In mathematics, a complex
    number is expressed in the form \( a + bi \), where \( a \) and \( b \) are
    real numbers, and \( i \) is the imaginary unit with the property that
    \( i^2 = -1 \). This unique property allows complex numbers to perform
    operations that cannot be handled by real numbers alone, such as taking the
    square root of a negative number.
    Complex numbers are pivotal in various fields, including engineering,
    physics, and applied mathematics, as they can represent phenomena like
    electrical currents and waves.
    Here are some examples of complex numbers:
    1. \( 3 + 4i \)
    1. \( -1 + 2i \)
    1. \( 5 - 3i \)
    1. \( 2i \) (This is a purely imaginary number, as the real part is 0.)
- **Boolean** (True or False) - Like answering a yes-no question.
- **Text** - Anything you can write in quotes.

### Compound Data Together

#### Lists

Just like your grocery list, where you can see many items in order:
```python
my_list = [apples, oranges, milk]
print(my_list[1])  # This shows 'oranges'
```

> The items on any list can be repeated without any constraints, It can contain
> even empty places.


#### Sets

Like a special storage box where you only keep one of each thing, no duplicates
are allowed:
```python
read_books = [
   "One Hundred Years of Solitude",
   "The Little Prince",
   "Crime and Punishment",
   "The Alchemist"
]
```

> Very useful when you want to avoid reading the same book twice.


#### Dictionaries

These are like personal address books where you store information that links a
meaningless phone number with the name of a person which may be friend or foe.

```python
my_book = {
   "name": "Alice",
   "number": "555-1234",
   "is_friend": True
}
```

#### Date and Times

- **Dates** are composed of 3 numbers depicting any calendar entries
  (e.g. `September 9, 2024`).
- **Times** are also 3 numbers refering to an exact moment in time
  (e.g. `15:34:01`).
- **Timestamps** a single integer number, telling you the exact number of
  seconds counting from a `January 1st, 1970`.

