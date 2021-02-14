#1
#ugly way, also given remains reversed
given = [100, 200, 300, 400, 500]
#expected = [500, 400, 300, 200, 100]
given.reverse()
expected = given
print("Ex.1 Ugly truth expected is",expected)
print("Ex.1 Ugly truth given is",given)

#pretty way :)
given = [100, 200, 300, 400, 500]
expected = []

for i in reversed(given):
    expected.append(i)

print("Ex.1 pretty way, expected is",expected)
print("Ex.1 pretty way, expected is",given)

#best
expected = [number for number in reversed(given)]
print("Ex.1 best way, expected is",expected)


#2
given = ["Mike", "", "Emma", "Kelly", "", "Brad"]
#expected = ["Mike", "Emma", "Kelly", "Brad"]
expected = [name for name in given if name != ""]
print("Ex.2 expected is", expected)

#3
given = [5, 10, 15, 20, 25, 50, 20]
#expected = [5, 10, 15, 200, 25, 50, 20]
flag=True
expected=[]
for number in given:
    if flag and number == 20:
        expected.append(number*10)
        flag=False
    else:
        expected.append(number)
print("Ex.3 1st idea, expected is",expected)

#2nd idea
flag=True
expected=[]
for number in given:
    if flag and given.index(number) == len(given)//2:
        expected.append(number*10)
        flag=False
    else:
        expected.append(number)
print("Ex.3 2nd and no better idea, expected is",expected)

#4
given = [5, 20, 15, 20, 25, 50, 20]
#expected = [5, 15, 25, 50]
expected = [name for name in given if name != 20]
print("Ex.4 expected is", expected)

#5
list1 = ["M", "na", "i", "Ri"]
list2 = ["y", "me", "s", "ck"]
#expected = ["My", "name", "is", "Rick"]
expected = [list1[0] + list2[0], list1[1] + list2[1],list1[2] + list2[2],list1[3] + list2[3]]
print("Ex.5 very ugly, expected is ",expected)

expected = [string1 + string2 for string1 in list1 for string2 in list2 if list1.index(string1) == list2.index(string2)]
print("Ex.5 awesome, expected is ",expected)
