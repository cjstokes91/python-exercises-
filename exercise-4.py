# exercise-04 What kind of Triangle?

# Write the code that:
# 1. Prompts the user to enter the three lengths of a triangle (one at a time):
#      Enter the lengths of three side of a triangle:
#      a: 
#      b:
#      c:
# 2. Write the code that determines if the triangle is:
#      equalateral - all three sides are equal in length
#      scalene - all three sides are unequal in length
#      isosceles - two sides are the same length
# 3. Print a message such as:
#      - A triangle with sides of <a>, <b> & <c> is a <type of triangle> triangle
# exercise-04 What kind of Triangle?
length = input('Enter the lengths of three side of a triangle:') 
a = input('a:')
b = input('b:')
c = input('c:')

if a == b ==c: 
    print(f'A trinagle with sides of {a} , {b} and {c} is a type of equalateral triangle')
elif a != b != c:
    print(f'A trinagle with sides of {a} , {b} and {c} is a type of scalene triangle')
else: 
    print(f'A trinagle with sides of {a} , {b} and {c} is a type of isolceles triangle')
    5

 