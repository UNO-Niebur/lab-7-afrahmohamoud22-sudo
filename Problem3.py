#Problem3.py
#Project Euler problem 3
#Name: Afrah Mohamoud 
#Date: 03/08/2026
#Assignment: Lab 7

#Approach: Build factor pairs up to sqrt(n), filter those factors to primes,
#          and take the largest prime factor.
#Runtime notes: Efficient for this input because factor search stops at sqrt(n).

def isPrimeLocal(p):
  """Returns True when p is prime."""
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


def allFactors(number):
  """Returns all factors of number in sorted order."""
  factors = set()

  for div in range(1, int(number ** 0.5) + 1):
    if number % div == 0:
      factors.add(div)
      factors.add(number // div)

  return sorted(factors)


def primeFactors(number):
  """Returns only the prime factors of number."""
  factors = allFactors(number)
  primes = []

  for value in factors:
    if isPrimeLocal(value):
      primes.append(value)

  return primes


def largestPrimeFactor(number):
  """Returns the largest prime factor of the given positive integer."""
  primes = primeFactors(number)
  return max(primes)


def main():
  number = 600851475143
  factors = allFactors(number)
  primes = primeFactors(number)
  answer = largestPrimeFactor(number)

  print("Factors:", factors)
  print("Prime factors:", primes)
  print("Largest prime factor:", answer)
  


if __name__ == '__main__':
  main()
