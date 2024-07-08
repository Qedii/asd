import math
while True:
    input1 = int(input("Enter : 1 for square, 2 for rectangle, 3 for circle  "))
    if input1 == 2:
        rows = int(input("enter the number of rows: "))
        columns = int(input("enter the number of columns: "))
        for i in range(rows):
            for x in range(columns):
                print(" * ", end="")
            print()


    elif input1 == 1:
        num = int(input("enter the number of rows: "))
        for i in range(1,num+1):
            print(" * "*num)


    elif input1 == 3:
        radius = int(input("Enter the radius: "))
        for x in range(-radius, radius + 1):
            for y in range(-radius, radius + 1):
                if radius - 1 <= math.sqrt(x ** 2 + y ** 2) <= radius:
                    print("*", end=" ")
                else:
                    print(" ", end=' ')
            print()


    else:
        print("try again")
    keep = int(input("Press 1 for continue, 0 to close the program  "))
    if keep == 1:
        continue
    elif keep == 0:
        break