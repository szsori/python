import math 

def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

missingVariable = input("Are you missing A, B, or C?\n")
if (missingVariable != "A" and missingVariable != "B" and missingVariable != "C"):
    print("Please enter A, B, or C")
    exit()

if (missingVariable == "A"):
    bString = input("Enter the value for B:\n")
    cString = input("Enter the value for C:\n")

    if (is_float(bString) == False or is_float(cString) == False):
        print("Please enter valid numbers for B and C")
        exit()

    b = float(bString)
    c = float(cString)

    missing = math.sqrt(c**2 - b**2)
    missingFormatted = str(float("{:.4f}".format(missing)))

if (missingVariable == "B"):
    aString = input("Enter the value for A:\n")
    cString = input("Enter the value for C:\n")

    if (is_float(aString) == False or is_float(cString) == False):
        print("Please enter valid numbers for A and C")
        exit()

    a = float(aString)
    c = float(cString)

    missing = math.sqrt(c**2 - a**2)
    missingFormatted = str(float("{:.4f}".format(missing)))

if (missingVariable == "C"):
    aString = input("Enter the value for A:\n")
    bString = input("Enter the value for B:\n")

    if (is_float(aString) == False or is_float(bString) == False):
        print("Please enter valid numbers for A and B")
        exit()

    a = float(aString)
    b = float(bString)

    missing = math.sqrt(a**2 + b**2)
    missingFormatted = str(float("{:.4f}".format(missing)))

print("The missing value is: " + missingFormatted)