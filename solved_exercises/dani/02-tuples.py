import itertools
'************************************************'
print('Check wether an element exists within a tuple')
my_tuple = 1, 2, 3, 3, 4, 5, 6
value = int(input("Please enter a numeric value:\n"))
if my_tuple.count(value)>0: print(value," is in my_tuple: ", my_tuple)
else: print(value," isn't in my_tuple: ", my_tuple)

'************************************************'
print('Sum up all the number elements within a tuple')
my_tuple = 1, 2, 3, 3, 4, 5, 6
print("Version1: sum of numbers in my_tupple is: ",sum(my_tuple))
'-------------------------------------------------'
my_tuple = 1,'2.2', 'a', 'asd2', 4, 5, 'a6'
my_tuple_nums = [tupla for tupla in my_tuple if isinstance(tupla,int)]
print("Version2: sum of numbers in my_tupple is:", sum(my_tuple_nums))

'************************************************'
print('Find the repeated items of a tuple')
my_tuple = 1, 2, 3, 3, 3, 5, 5, 6
my_multiples = [item for item in my_tuple if my_tuple.count(item)>1]
print('items that are multiple are:',my_multiples)

'************************************************'
print('Print out all pair combinations of two tuples')
tuple1 = 'a','b','c'
tuple2 = 'd','e'
print('tuple1 is ', tuple1)
print('tuple2 is', tuple2)
print('Version1 Works only for strings',[''.join(x) for x in itertools.product(tuple1, tuple2)])
'-------------------------------------------------'
tuple1 = 1,'2','a'
tuple2 = 3,'4','b'
print('tuple1 is ', tuple1)
print('tuple2 is', tuple2)
print('Version 2 Works with numbers and strings',list(itertools.product(tuple1, tuple2)))