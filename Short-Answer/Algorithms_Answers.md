#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

## For example's sake, instances of 'n' will = 2. 
## Anything in '' is referential to the questions from Algorithms_Answers. 

a) 'while (a < n * n * n):'
    2 * 2 * 2 = 8

    'a = a + n * n'
     a = 0 + 2 * 2 = 4
     a = 4

     The while loop repeats until 'a' is no longer greater than 'n * n * n'
     Resulting in: 
     a = 12 

    The runtime is O(n) by Iteration 


b)'sum = 0'
  'for i in range(n):'
    i in the range of 2

    'j = 1'
      'while j < n:'
    1 < 2

    'j *= 2'
     j = j * 2
     j = 2

        'sum += 1'
        0 = 0 + 1
        sum = 1

    I'm unsure on this one but i'll say O(n), x in s

c) In this case, bunnies will = 5

    'def bunnyEars(bunnies):'
      'if bunnies == 0:'
        'return 0'
    Bunnies will return 0 if the value is zero, in this case it doesn't.

      'return 2 + bunnyEars' 
      bunnyEars will hold an intrinsic value of 2 for
      each instance of bunnies

        '(bunnies-1)
        The value of bunnies is reduced by 1,
        resulting in 4 bunnies, meaning 8 bunnyEars

## Exercise II

def building (n, f):

  if n 
