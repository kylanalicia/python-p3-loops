#!/usr/bin/env python3

def happy_new_year():
    counter = 10
    while counter > 0:
     print (counter)
    print("Happy New Year!")

def square_integers(int_list):
    return [num ** 2 for num in int_list]

integer_list = [1, 2, 3, 4, 5]
squared_list = square_integers(integer_list)
print(squared_list)

def fizzbuzz_printer():
    for num in range(1, 101):
        print(fizzbuzz(num))

def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num

fizzbuzz_printer()
