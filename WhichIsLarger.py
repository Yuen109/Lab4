# Read A,B,C
A = int(input("Enter number A:"))
B = int(input("Enter number B:"))
C = int(input("Enter number C:"))

if A > B:
    max = A
else:
    max = B
if C > max:
    max = C
if A < B:
    min =A
else:
    min = B
if C < min:
    min = C

print("max is %10d, and min is %10d"%(max,min))
