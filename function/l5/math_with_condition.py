import math  #importing math module

x = float('nan')
if math.isnan(x): #to check whether the given value is number or not
    print('It is not a number')
x = float('inf')
y = 45
if math.isinf(x): #to check whether the given number is infinite or not
    print('It is Infinity')
print(math.isfinite(x)) #x is not a finite number
print(math.isfinite(y)) #y is a finite number
print(math.isnan(y))
