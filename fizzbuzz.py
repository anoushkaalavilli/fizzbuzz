"""
fizzbuzz.py
Author: Anoushka Alavilli
Credit: no one

Assignment:

Write a program that prints the numbers from 1 to 100. But for 
multiples of three print “Fizz” instead of the number and for 
the multiples of five print “Buzz”. For numbers which are multiples 
of both three and five print “FizzBuzz”.

We will use a variation of this test in which the last number of 
the series isn't necessarily 100, and the two numbers being tested 
for multiples aren't necessarily three and five. For example, your 
program should behave just like this:

How many numbers shall we print? 25
For multiples of what number shall we print 'Fizz'? 3
For multiples of what number shall we print 'Buzz'? 5
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
16
17
Fizz
19
Buzz
Fizz
22
23
Fizz
Buzz
"""
numberofnumbers= input("How many numbers shall we print? ")
fizz= input("For multiples of what number shall we print 'Fizz'? ")
buzz= input("For multiples of what number shall we print 'Buzz'? ")
number= int(numberofnumbers)
intfizz= int(fizz)
intbuzz= int(buzz)

for i in range(1,((number)+1)):
    if i%3==0 and i%5==0:
        print ("FizzBuzz")
    elif i%3==0:
        print ("Fizz")
    elif i%5==0:
        print ("Buzz")
    else:
        print (i)







