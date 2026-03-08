#Problem2.py
#Project Euler problem 2
#Name: Afrah Mohamoud 
#Date: 03/08/2026
#Assignment: Lab 7

#Approach: Build Fibonacci values below 4,000,001 using reusable helper
#          functions, then sum only even terms.
#Runtime notes: Fast for this limit because the Fibonacci list is small.

from NumberTests import isEven
from NumberTests import fibonacciSequence

def main():
  nums = fibonacciSequence(4000001)
  print (nums)
  total = 0
  for fib in nums:
    if isEven(fib):
      total = total + fib
  
  print(total) # final answer

if __name__ == '__main__':
  main()
