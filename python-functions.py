# Problem 1 - Write a function named sum_to that accepts a single integer, n, and returns the sum of the integers from 1 to n.

def sum_to( n ):
  return sum(range(n + 1))

print('Answer for Problem-1 (using 6):',sum_to(6))
print('Answer for Problem-1 (using 10):',sum_to(10))

# Problem 2 - Write a function named largest that takes a list of numbers as an argument and returns the largest number in that list.

def largest ([])