
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
    1. 3 + 4j
    1. -1 + 2j
    1. 5 - 3j
    1. 2j _This is a purely imaginary number, as the real part is 0._
- **Boolean** (True or False) - Like answering a yes-no question.
- **Text** - Anything you can write in quotes.

### Compound Data Together

#### Lists

Just like your grocery list, where you can see many items in order:
```python
healthy_fruits = [apples, oranges, berries]
# position:        [0]      [1]      [2]

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


## Control flow structures

Structured programming is a programming paradigm aimed at improving the clarity,
quality, and development time of a computer program by making extensive use of
the structured control flow constructs of selection (if/then/else) and repetition
(while and for), block structures, and subroutines (aka functions). 

### Sequence

A list of statements (commands) to be executed in order.

```python
a = 100
print("hello")
print(a)
b = "hello"
c = "world"
print(b, c)
```

### Selection

Selection allows a program to make choices and execute certain blocks of code based
on specific conditions. The most common selection structures are `if`, `else`, and `elif`
(short for "else if").

These help the program decide which path to take based on the given input or data.
```python
today = int(input("What day is today?")

if 5 <= today <= 9:
    print(4, "Oh, this means salary day!")
    print(5, "let's all go for a beer...")
    who_pays = input("Who pays?")
    print(6, "The lucky funding VC is", who_pays, "!")
    total = 107
    print(8, "total is", total)
else:
    # else is not mandatory, place it here only when you have something to do
    pass
    # notice python supports pass, as a command that does nothing
```


How it works:
1. If statement:
   The _if_ statement checks whether a condition is _True_. If it is, the code inside
   the _if_ block gets executed. Otherwise, if the condition is _False_, the program
   skips that block of code.
1. Elif statement:
   The _elif_ block allows you to check multiple conditions. If the first if condition
   is _False_, Python will check the next _elif_ block, and so on.
1. Else statement:
   The _else_ block executes if none of the if or elif conditions are true. It's like
   a "catch-all" block that ensures some code is executed, even if the conditions
   aren’t met.

For example:
```python
temperature = 25

if temperature > 30:
    print("It's a hot day.")
elif temperature > 20:
    print("It's a warm day.")
else:
    print("It's a cold day.")
```

A lighter flavor of selection structure is _assertion_ which is an assumption check,
it let's program continue only if the _asserted_ condidtion is _True_.

```python
today = input("what day of the month is today?")
assert today.isnumeric(), "Expected a numeric value."
```

Please read [this related section](https://python-1o1-tutorial.readthedocs.io/en/latest/logical.html#falsy-values)
for more details of these _falsy_ values.

```python
falsy_val_1 = ""
falsy_val_2 = 0
falsy_val_3 = []
falsy_val_4 = {}
falsy_val_5 = False
falsy_val_6 = 0.0
print(falsy_val_1, type(falsy_val_1), bool(falsy_val_1))
print(falsy_val_2, type(falsy_val_2), bool(falsy_val_2))
print(falsy_val_3, type(falsy_val_3), bool(falsy_val_3))
print(falsy_val_4, type(falsy_val_4), bool(falsy_val_4))
print(falsy_val_5, type(falsy_val_5), bool(falsy_val_5))
print(falsy_val_6, type(falsy_val_6), bool(falsy_val_6))
```

And now is a good moment to walkthrough this
[entire lesson](https://python-1o1-tutorial.readthedocs.io/en/latest/logical.html)


### Iteration

Iteration is a way for a program to repeat certain instructions multiple times.
The repetition can either be over a set of items (using a `for` loop) or based on a
condition (using a `while` loop).

Traversing any list is called _iteration_ and is uses the `for` keyword

You can use a `for` loop when you know the number of iterations or want to repeat
a block of code for each item in a list or sequence. The loop automatically goes through
each element in the sequence until all elements are processed.

```
movies = ["7even", "Star Trek", "Long Lex"]
for movie in movies:
    print(movie)
```

Inside any block you nest any kind of structures:
```python
colors = ["red", "blue", "green"]
for color in colors:
    print(color)


movies = [
    "Star Wars", "Ghandi", "Casablanca", "Shawshank Redemption",
    "Toy Story", "Gone with the wind", "Citizen Kane", "It's a wonderful life",
    "The Wizard of Oz", "Gattaca", "Rear Window", "Ghostbusters",
    "To Kill a Mockingbird", "Good Will Hunting", "2001: A Space Odissey",
    "Riders of the Lost Ark", "Groundhog Day",
    "Close Encounters of the Third King", "Scent of a Woman",
]

g_movies = []
the_movies = []
for title in movies:
    # you can go crazy with the nesting
    if title.startswith("The"):
        the_movies.append(title)
    elif title.startswith("G"):
        g_movies.append(title)
```

### Repetition

A while loop repeats as long as a condition is true. The condition is checked before
each iteration, and the loop will continue running until the condition becomes false.

```python
# repeat sequence until the user enters 0
number = 1
while number != 0:
    number = int(input('Enter a number: '))
    print(f'You entered {number}.')
print('Let's stop now.')

# countdown from 5 to 1 before yelling "Happy new year!"
counter = 5
while counter > 0:
    print(counter)
    counter -= 1
print("Happy new year!")
```

> Infinite Loops:
> Be cautious with while loops! If the condition never becomes false, the loop will
> run forever, which can cause the program to freeze or crash. For example:
> ```python
> while True:
>    print("This loop will run forever!")
> ```
> This loop will never stop because True is always true and most likely our program will freeze.
