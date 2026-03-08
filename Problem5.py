#Problem5.py
#Project Euler problem 5
#Name: Afrah Mohamoud 
#Date: 03/08/2026
#Assignment: Lab 7

#Approach: Use a sieve(2) to mark non-primes, then sum the values still marked prime.
#Runtime notes: Efficient for the 2,000,000 limit.

def sumPrimesBelow(limit):
  """Returns the sum of all prime numbers below limit."""
  if limit <= 2:
    return 0

  sieve = [True] * limit
  sieve[0] = False
  sieve[1] = False

  for num in range(2, int(limit ** 0.5) + 1):
    if sieve[num]:
      start = num * num
      for multiple in range(start, limit, num):
        sieve[multiple] = False

  total = 0
  for value in range(2, limit):
    if sieve[value]:
      total += value

  return total


def main():
  answer = sumPrimesBelow(2000000)
  print(answer)


if __name__ == '__main__':
  main()
