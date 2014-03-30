Python 3.2.3 (default, Oct 19 2012, 20:10:41) 
[GCC 4.6.3] on linux2
Type "copyright", "credits" or "license()" for more information.
==== No Subprocess ====
>>> location = input('What is your location? ')
What is your location? Prague
>>> name = input('What is your name? ')
What is your name? Ilir
>>> print(name, 'lives in', location)
Ilir lives in Prague
>>> greeting = '''How
are
you'''
>>> greeting
'How\nare\nyou'
>>> print('3\t4\t5')
3	4	5
>>> print('\\')
\
>>> print('Hello\nworld')
Hello
world
>>> 
>>> convert_to_celsius(32)
0.0
>>> 
>>> help(convert_to_celsius)
Help on function convert_to_celsius in module __main__:

convert_to_celsius(fahrenheit)
    (number) -> float
    
    Return the number in Celsius degrees equivalent of "fahrenheit" degrees.
    >>> convert_to_celsius(32)
    0.0
    >>> convert_to_celsius(212)
    100.0

>>> convert_to_celsius(212)
100.0
>>> 
>>> semiperimeter(3, 4, 5)
6.0
>>> help(semiperimeter)
Help on function semiperimeter in module __main__:

semiperimeter(side1, side2, side3)
    (number, number, number) -> float
    
    Return the semiperimeter of the triangle with sides of
    length side1, side2, and side3.
    
    >>> semiperimeter(3, 4, 5)
    6.0
    >>> semiperimeter(10.5, 6, 9.3)
    12.9

>>> semiperimeter(10.5, 6, 9.3)
12.9
>>> max(area(3.8, 7.0), area(3.5, 6.8))
13.299999999999999
>>> area(3.8, 7)
13.299999999999999
>>> 4 > 3
True
>>> 4 > 9
False
>>> 3 = 3.0
SyntaxError: can't assign to literal
>>> 3 == 3.0
True
>>> x = 7
>>> y = 8
>>> x == y
False
>>> x != y
True
>>> grade = 80
>>>  grade >= 50
 
SyntaxError: unexpected indent
>>> grade >= 50
True
>>> not(grade >= 50)
False
>>> not not(grade >= 50)
True
>>> grade2 = 70
>>> (grade >= 50) and (grade2 >= 50)
True
>>> grade = 40
>>> grade = 40
>>> (grade >= 50) and (grade2 >= 50)
False
>>> grade = 80
>>> grade2 = 90
>>> not (grade >= 50) or (grade2 >= 50)
True
>>> not (grade >= 50 or grade2 >= 50)
False
>>> not grade >= 50
False
>>> type(True)
<class 'bool'>
>>> three = str(3)
>>> three
'3'
>>> int(three*5)
33333
>>> str(4.65)
'4.65'
>>> int(3.5)
3
>>> int(3.99)
3
>>> num_shoes_left = 627
>>> int(input("Enter the number of shoes: ")
    )
Enter the number of shoes: 888
888
>>> import math
>>> dir(math)
['__doc__', '__name__', '__package__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'copysign', 'cos', 'cosh', 'degrees', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'hypot', 'isfinite', 'isinf', 'isnan', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'modf', 'pi', 'pow', 'radians', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'trunc']
>>> help(math.sqrt)
Help on built-in function sqrt in module math:

sqrt(...)
    sqrt(x)
    
    Return the square root of x.

>>> 
>>> area_hero(3, 4, 5)
6.0
>>> area_hero(10.5, 6, 9.3)
27.73168584850189
>>> 
