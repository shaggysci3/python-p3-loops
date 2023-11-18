#!/usr/bin/env python3

def happy_new_year():
    i=10
    while i > 0:
        print(i)
        i -= 1
    print("Happy New Year!")
    



def square_integers(int_list):
    list1 = []
    for i in int_list:
        list1.append(i**2)
    return list1

def fizzbuzz():
    for i in range(1,101):
        n = fizzbuzzE(i)
        print(n)

# Write a function `fizzbuzz()` that prints the numbers from 1 to 100. For
# multiples of three, print "Fizz" instead of the number and for the multiples
# of five print "Buzz". For numbers which are multiples of both three and five,
# print "FizzBuzz".

def fizzbuzzE(num):
    if num%3 == 0 and num%5 == 0: 
      return   "FizzBuzz"
    elif num%3 == 0:
        return "Fizz"
    elif num%5 ==0:
        return "Buzz"
    return num
