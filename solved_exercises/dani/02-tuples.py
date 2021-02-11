import itertools
'''*********************************************************************************************'''
print('*****************Check wether an element exists within a tuple******************')
my_tuple = 1, 2, 3, 3, 4, 5, 6
print('my_tuple is', my_tuple)
a=3
b=7
print('Version1')
print (a in my_tuple and (a," is in my_tuple") or (a," isn't in my_tuple"))
print (b in my_tuple and (b," is in my_tuple") or (b," isn't in my_tuple"))
'''---------------------------------------------------------------------------'''
print('Version2')
print(my_tuple.count(a) and (a," is in my_tuple") or (a," isn't in my_tuple"))
print(my_tuple.count(b) and (b," is in my_tuple") or (b," isn't in my_tuple"))

'''*********************************************************************************************'''
print('***************Sum up all the number elements within a tuple********************')
my_tuple = 1, 2, 3, 3, 4, 5, 6
print("Version 1: sum of the numbers in my_tupple", my_tuple, "is: ",sum(my_tuple))
'''---------------------------------------------------------------------------'''
my_tuple = 1,'2', 'a', 'asd2', 4, 5, 'a6'
suma = [tupla for tupla in my_tuple if isinstance(tupla,int)]
print("Version 2: sum of the numbers in my_tupple ", my_tuple, "is: ", sum(suma))

'''*********************************************************************************************'''
print('**********************Find the repeated items of a tuple*******************')
my_tuple = 1, 2, 3, 3, 3, 5, 6
print('element 7 is ',my_tuple.count(7), 'times in my tuple')
print('element 3 is ',my_tuple.count(3), 'times in my tuple')

'''*********************************************************************************************'''
print('*****************Print out all pair combinations of two tuples*************')
tuple1 = 'a','b','c'
tuple2 = 'd','e'
print('tuple1 is ', tuple1)
print('tuple2 is', tuple2)
print('Version 1 Works only for strings',[''.join(x) for x in itertools.product(tuple1, tuple2)])
'''---------------------------------------------------------------------------'''
tuple1 = 1,'2','a'
tuple2 = 3,'4','b'
print('tuple1 is ', tuple1)
print('tuple2 is', tuple2)
print('Version 2 Works with numbers and strings',list(itertools.product(tuple1, tuple2)))