"""lists continued, tuples, sets"""
"""functions dictionaries"""

# in operator (also not in)
given2 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
while "" in given2:
    given2.remove("")


# how about more complex examples
expected = [
    string1 + string2       # expression
    for string1 in list1    # collection(s)
    for string2 in list2
    if list1.index(string1) == list2.index(string2)   # condition
]


# tuples are immutable lists
movies = [
        ("Citizen Kane", 1941), ("Spirited Away", 2001),
        ("It's a wonderful life", 1946), ("Gattaca", 1997),
        ("No Country for Old Men", 2007), ("Rear Window", 1954),
        ("The Lord of the Rings: The Fellowship of the Ring", 2001),
        ("Groundhog Day", 1993), ("Close Encounters of the Third King", 1977),
        ("The Aviator", 2004), ("Riders of the Lost Ark", 1981),
    ]

dumb_movies = [
        ["Citizen Kane", 1941], ["Spirited Away", 2001],
        ["It's a wonderful life", 1946], ["Gattaca", 1997],
        ["No Country for Old Men", 2007], ["Rear Window", 1954],
        ["The Lord of the Rings: The Fellowship of the Ring", 2001],
        ["Groundhog Day", 1993], ["Close Encounters of the Third King", 1977],
        ["The Aviator", 2004], ["Riders of the Lost Ark", 1981],
    ]


pre2k = [title for title, year in movies if year < 2000]

for title, year in dumb_movies:
    print(title, year)
    year = 9999


for iterator in dumb_movies:
    print(iterator)
    iterator[1] = 9999
