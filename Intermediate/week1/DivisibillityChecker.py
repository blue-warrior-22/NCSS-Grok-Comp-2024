def divisibility_checker(dividend, divisor):
    a = dividend % divisor
    if a == 0:
        c = True
    else:
        c = False
    return c

while True:
    b = int(input("Enter an integer Dividend: "))
    c = int(input("Enter an integer Divisor: "))
    a = divisibility_checker(b,c)
    if a == True:
        print(f"{b} is a multiple of {c}")
    else:
        print(f"{b} is not a multiple of {c}")
    