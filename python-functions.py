# Problem 1 - Write a function named sum_to that accepts a single integer, n, and returns the sum of the integers from 1 to n.

def sum_to( n ):
  return sum(range(n + 1))

print('Answer for Problem-1 (using 6):',sum_to(6))
print('Answer for Problem-1 (using 10):',sum_to(10))

# Problem 2 - Write a function named largest that takes a list of numbers as an argument and returns the largest number in that list.

def largest (numbers):
  max = numbers[0]
  for number in numbers:
    if number > max:
      max = number
  return max

print('Answer for Problem-2:',largest([1, 2, 3, 4, 0]))
print('Answer for Problem-2:',largest([10, 4, 2, 231, 91, 54]))

# Problem 3 - Write a function named `occurances` that takes two string arguments as input and counts the number of occurances of the second string inside the first string.


def occurances (words, letter):
  count = words.count(letter)
  return count

print('Answer for Problem-3:',occurances('fleep floop', 'e'))
print('Answer for Problem-3:',occurances('fleep floop', 'p'))
print('Answer for Problem-3:',occurances('fleep floop', 'ee'))
print('Answer for Problem-3:',occurances('fleep floop', 'fe'))

# Problem 4 - Write a function named product that takes an arbitrary number of numbers, multiplies them all together, and returns the product. HINT: Review your notes on args.

def product (*args):
  number = 1
  for arg in args:
    number *= arg
  return number    

print('Answer for Problem-4:', product(-1, 4)) 
print('Answer for Problem-4:', product(2, 5, 5)) 
print('Answer for Problem-4:', product(4, 0.5, 5)) 

