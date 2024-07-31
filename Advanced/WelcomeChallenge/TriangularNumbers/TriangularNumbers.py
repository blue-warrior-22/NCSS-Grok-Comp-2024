limitn = int(input("Limit: "))
number = 0
i = 0
while number <= limitn:
    number = number + i
    if number <= limitn:
        if number != 0:
            print(number)
    i+=1