from datetime import datetime
import timeit

def fizzbuzz_1():
    listamea = []
    for i in range(1, 101):
        result = ""
        if i % (3 * 5) == 0:
            #print("fizzbuzz")
            result = "fizzbuzz"
        elif i % 3 == 0:
            result = "fizz"
            #print("fizz")
        elif i % 5 == 0:
            result = "buzz"
            #print("buzz")
        else:
            result = str(i)
            #print(i)
        listamea.append(result)
    return listamea

def fizzbuzz_2():
    listamea = []
    for i in range(1, 101):
        if i % 3 == 0:
            if i % 5 == 0:
                #print("fizzbuzz")
                result = "fizzbuzz"
            else:
                result = "fizz"
                #print("fizz")
        elif i % 5 == 0:
            result = "buzz"
            #print("buzz")
        else:
            result = str(i)
            #print(i)
        listamea.append(result)
    return listamea

def fizzbuzz_3():
    listamea = []
    for i in range(1, 101):
        result = ""
        is_divisible_by_3 = i % 3 == 0
        is_divisible_by_5 = i % 5 == 0
        if is_divisible_by_3 and is_divisible_by_5:
            #print("fizzbuzz")
            result = "fizzbuzz"
        elif is_divisible_by_3:
            #print("fizz")
            result = "fizz"
        elif is_divisible_by_5:
            #print("buzz")
            result = "buzz"
        else:
            #print(i)
            result = str(i)
        listamea.append(result)
    return  listamea

def fizzbuzz_4():
    listamea = []
    for i in range(1, 101):
        result = ""
        is_divisible_by_3 = i % 3 == 0
        is_divisible_by_5 = i % 5 == 0
        if is_divisible_by_3:
            result = "fizz"
        if is_divisible_by_5:
            result += "buzz"
        if not result:
            result = str(i)
        listamea.append(result)
    return listamea

def fizzbuzz_5():
    listamea = []
    modulo_list = [
                (3,"Fizz"),
                (5,"Buzz")
                ]

    for i in range(1, 101):
        print_string = ""
        for mod in modulo_list:
            if i % mod[0] == 0:
                print_string += mod[1]

        if print_string == "":
            #print(i)
            listamea.append(str(i))
        else:
            #print(print_string)
            listamea.append(print_string)
    return listamea

def main():
    duration1 = timeit.timeit(fizzbuzz_1, number=100000)
    duration2 = timeit.timeit(fizzbuzz_2, number=100000)
    duration3 = timeit.timeit(fizzbuzz_3, number=100000)
    duration4 = timeit.timeit(fizzbuzz_4, number=100000)
    print(f'Finished fizzbuzz_1 in {duration1:.10f} seconds.')
    print(f'Finished fizzbuzz_2 in {duration2:.10f} seconds.')
    print(f'Finished fizzbuzz_3 in {duration3:.10f} seconds.')
    print(f'Finished fizzbuzz_4 in {duration4:.10f} seconds.')


if __name__ == "__main__":
    main()


