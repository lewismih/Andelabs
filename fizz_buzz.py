# Create a function fizz_buzz that returns a statement or value depending on the argument it receives
def fizz_buzz (x):
  
  if (x % 15 == 0):
    return 'FizzBuzz'
  
  if (x % 3 == 0 ):
    return 'Fizz'
  
  elif (x % 5 == 0 ):
    return 'Buzz'
    
  
    
  else:
    return x