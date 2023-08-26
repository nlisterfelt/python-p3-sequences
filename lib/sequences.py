#!/usr/bin/env python3

def print_fibonacci(length):
    if(length==0):
        print([])
    elif(length==1):
        print([0])
    elif(length==2):
        print([0,1])
    elif(length==3):
        print([0,1,1])
    else:
        i=3
        fib_list=[0,1,1]
        while i<length:
            num1 = fib_list[i-2]
            num2 = fib_list[i-1]
            fib_list.append(num1+num2)
            i += 1
        print(fib_list)