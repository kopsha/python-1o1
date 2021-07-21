a = 42
b = 10
c = 0
try:
    remainder = (a + b) // c 
except (TypeError, NameError) as err:
    print(f"Cannot sum the variables, reason: {err}.")
except Exception as err:
    print(f"A {type(err)} occurred, please inspect: {err}.")

