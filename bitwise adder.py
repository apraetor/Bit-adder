
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
    strAdd = adder(strA, strB)
    strCarry = carry(strA, strB)
    # using intermediate vars because adder() and carry() must both be called
    # prior to vars updating
    strA = strAdd
    strB = strCarry


print("Sum: {0:b}".format(strA))
