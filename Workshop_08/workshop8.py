'''
Author: Akond Rahman 
Code needed for Workshop 8
'''

from ast import operator
import random 

def divide(v1, v2):
    temp = 0 
    if (isinstance(v1, int))  and (isinstance(v2, int)): 
       if v2 >  0:
          temp =  v1 / v2
       elif v2 < 0:
          temp = v1 / v2 
       else:
          # Updated print to return for output reasons. 
          temp = "Divisor is zero. Provide non-zero values."
    else: 
       temp = "Invalid input. Please provide numeric values."    
    return temp 

def fuzzValues():
    # positive or expected software testing 
    #res = divide(2, 1)
    # negative software testing: > 0 divisor test 
    #res = divide(2, 0)
    # negative software testing: <0 divisor test 
    #res = divide(2, -1)
    # negative software testing: check types: example 1  
    #res = divide(2, '1')  
    # negative software testing: check types: example 2 
    #res = divide('2', '1') 
    
    # Note - negative and positive negative integers were removed from list because they would return without error. 
    # ..these were also previously tested in the commented out code above. 
    fuzzList = [0, 0.0, 1/2, -1.0, 'true', 'false', '🇺🇸', 'nil', '\t', '$', '', '(╯°□°）╯︵ ┻━┻)']
    
    # Iterator that randomly assigns a value to v1 and v2 from the fizzList and runs the divide method
    for fuzzies in range(7):
      v1 = random.choice(fuzzList)
      v2 = random.choice(fuzzList)
      res = divide(v1, v2)

      # Print the values and the result of the divide function
      print('v1 = {}, v2 = {}, res = {}'.format(v1, v2, res))
      print('='*100)

def simpleFuzzer(): 
    fuzzValues()

if __name__=='__main__':
    simpleFuzzer()