# entering sides of triangle
a = int(input("enter the 1st side of the triangle: "))
b = int(input("enter the 2nd side of the triangle: "))
c = int(input("enter the 3rd side of the triangle: "))
# Check triangle validity
if (a <= 0 or b <= 0 or c <= 0):
    print("TRIANGLE'S SIDE CANNOT BE ZERO or NEGATIVE \nIT SHOULD BE POSITIVE")
elif a + b <= c or a + c <= b or b + c <= a:
    print("NOT A VALID TRIANGLE")
else:
    s = (a + b + c) / 2
    s1=a+b+c #perimeter
    area=(s*(s-a)*(s-b)*(s-c))**0.5
    sides = sorted([a, b, c])
    # type,area and perimeter of the triangle
    if sides[2]**2 == sides[0]**2 + sides[1]**2:
        print("IT IS A RIGHT-ANGLED TRIANGLE")
        print("PERIMETER:",s1)
        print("AREA:", area)
    elif (a == b and b==c and c==a):
        print("IT IS AN EQUILATERAL TRIANGLE")
        print("PERIMETER:",s1)
        print("AREA:", area)
    elif (a == b or b == c or c == a):
        print("IT'S AN ISOSCELES TRIANGLE")
        print("PERIMETER:",s1)
        print("AREA:", area)
    else:
        print("IT'S A SCALENE TRIANGLE")
        print("PERIMETER:",s1)
        print("AREA:", area)