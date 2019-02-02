#!/usr/bin/python
# -*- coding: utf-8 -*-
 
MIN = 1000000
 def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True    else:
        if n % 2 == 0 or n % 3 == 0:
            return False    
 
    i = 5        while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
                  return False
        i += 6
    return True 
i = MIN 
k = 0           
while (k < 2):
    if is_prime(i):        sum_i = sum(map(int, str(i)))
        if is_prime(sum_i):
            print i
            k += 1            
    i += 1
