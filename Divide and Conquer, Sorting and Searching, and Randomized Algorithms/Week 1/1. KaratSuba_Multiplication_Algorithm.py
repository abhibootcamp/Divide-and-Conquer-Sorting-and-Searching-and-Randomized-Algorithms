# KaratSuba Multiplication Algorithm
import math
def product(x,y):
    
    # First make copy of x as a string such that it is used to determine the length of total number of digit in a number
    str_x = str(x)
    str_y = str(y)
    
    # This is the terminal condition of Recursive Relation if any of a number have length of digit equal to 1
    if (len(str_x) == 1) or (len(str_y) == 1):
        return x*y
    
    # Evaluating half length of number we sure to take ceil value if a/2 = 1.5 then take value as 2 not 1.5
    n1 = math.ceil(len(str_x)/2)
    n2 = math.ceil(len(str_y)/2)
    
    # Evaluating a and b from the number x suppose if x=5678 then a=56 and b=78
    a = int(x // math.pow(10 , n1))
    b = int(x %  math.pow(10 , n1))
    
    # Similarily Evaluating c and d from y
    c = int(y // math.pow(10 , n2))
    d = int(y %  math.pow(10 , n2))

    
    # now apply the equation
    # (10^n1 * a + b)(10^n2 * c + d)
    # (10^(n1+n2) * a * c) + (10^n1 * a * d) + (10^n2 * b * c)+(b * d)
    res = (math.pow(10,(n1+n2)) * product(a,c))
    
    res = res + (math.pow(10,n1) * product(a,d))
    
    res = res + (math.pow(10,n2) * product(b,c))

    res = res + product(b,d)
    return res
    
x = 5678
y = 1234
z = product(x,y)
print(z)