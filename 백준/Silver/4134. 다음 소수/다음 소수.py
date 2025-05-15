import sys
import math

input = sys.stdin.readline

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

def find_prime_list_under_number(number):
    while True:
        if is_prime(number):
            return number
        number += 1

tc = int(input())

for _ in range(tc):
    n = int(input())
    result = find_prime_list_under_number(n)
    print(result)
