
# Structured programming basics

## Programming pyramid

```
# highest level -> functional & business logic (application, server,
## frameworks (django be, react fe)
### python / javascript / net (backend - api & db vs frontend - browser)
#### data & behavior (non-hardware)
##### - low level -> hardware (cpu, network, video)
websites)
```

## Programming buiding blocks

1. data (values and its meaning)
2. behavior (actions & decisions / conditions)
`if some question then do some action`

add, substract, multiply, divide -> read/write to memory

--> interpretarea datelor -> information has meaning


invoice -> nr, status -> created -> 1, accepted -> 2, rejected -> 3, paid -> 4
JIBE-000x, "created"
text / numeric / text
text / numeric / numeric

###. Basic data types (relies on binary 0/1)
- none (null, undefined)
- numeric (price, tax, interest,) -> digit 0-9 number: multiple digits
  - integer (-2, -1, 0, 1, 2, 123.... ) Z
  - floats (0.01, 2.3, 3.3333) Q
  - complex (a + b * j)
- boolean (logic) -> true / false (10 > 22)
- character (text) -> "text is always in quotes" ('this is also text')



###. Compound data types

1. datetime (date + time)
  - date (D/M/Y 3 numbers, UTC)
  - time (h:m:s/ms/us 3/4/5 numbers, UTC)
  - timestamp (seconds since jan-01 1970)

2. lists (array) - joining multiple data togetether

odd_numbers = [1, 3, 5, 7, 9] -> parcurge, access prin pozitie
               0  1  2  3  4
odd_numbers[2]
5 elemente odd_numbers[5-1] -> Out of bounds exception

any_numbers = [1, 1, 1, 2, 2] -> parcurge, access prin pozitie
               0  1  2  3  4

3. sets       {1, 2, 13, 14}

4. dictionaries (key value pairs) (struct)
{
    cuvant: explicatie (value),
    cuvant: explicatie (value),
    cuvant: [explicatie 0, 1, 2, ...]
}
{
    date_issued: timestamp,
    series: text,
    number: number,
    items: list,
    currency: text,
    total_price: 0.00000000,
    vat: float,
    status: text,
    paid: true,
}
