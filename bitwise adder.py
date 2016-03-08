
# user input
strA = int(input("First: "), base=2)
strB = int(input("Second: "), base=2)


# AND of two values, left shift by 1
def carry(strA, strB):
    return (strA & strB) << 1


# XOR of two values
def adder(strA, strB):
    return strA ^ strB

while (strB > 0):
    strA1 = adder(strA, strB)
    strB1 = carry(strA, strB)
    strA = strA1
    strB = strB1


print("Sum: {0:b}".format(strA))
