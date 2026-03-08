#Problem4.py
#Project Euler problem 4
#Name: Afrah Mohamoud 
#Date: 03/08/2026
#Assignment: Lab 7

#Approach: Check each candidate for primality and count primes until the
#          10001st prime is found.
#Runtime notes: Fast enough for n = 10001 using sqrt(n) checks and skipping evens.

def isPrime(p):
  """Returns True if p is prime, otherwise False."""
  if p < 2:
    return False
  if p == 2:
    return True
  if p % 2 == 0:
    return False

  for div in range(3, int(p ** 0.5) + 1, 2):
    if p % div == 0:
      return False

  return True


def nthPrime(n):
  """Returns the nth prime number (1-based index)."""
  count = 0
  candidate = 1

  while count < n:
    candidate += 1
    if isPrime(candidate):
      count += 1

  return candidate


def main():
  answer = nthPrime(10001)
  print(answer)


if __name__ == '__main__':
  main()