f = open("locked_loans.txt")

locked_ids = f.readlines()
locked_ids.__contains__(locked_ids)

print(locked_ids)

x = open("waiver_0.txt")

file_ids = x.readlines()
file_ids.__contains__()

print(file_ids)


for el in locked_ids:
  file_ids = open("waiver_0.txt")
  if file_ids.__contains__(el):
    print(...)
  file_ids.close()

















#import math
#from colorama import Fore
#while True:
#    input1 = int(input("Enter : 1 for square, 2 for rectangle, 3 for circle  "))
#    input2 = int(input("CHANGE the color: 4 for red, 5 for green, 6 for yellow, 7 for blue "))
#    if input2==4:
#        print(Fore.RED)
#    if input2==5:
#       print(Fore.GREEN)
#    if input2==6:
#        print(Fore.YELLOW)
#    if input2==7:
#        print(Fore.BLUE)
#    if input1 == 2:
#        rows = int(input("enter the number of rows: "))
#        columns = int(input("enter the number of columns: "))
#        for i in range(rows):
#            for x in range(columns):
#                print(" * ", end="")
#            print()
#
#    elif input1 == 1:
#        num = int(input("enter the number of rows: "))
#        for i in range(1,num+1):
#            print(" * "*num)
#

#    elif input1 == 3:
#        radius = int(input("Enter the radius: "))
#        for x in range(-radius, radius + 1):
#            for y in range(-radius, radius + 1):
#                if radius - 1 <= math.sqrt(x ** 2 + y ** 2) <= radius:
#                    print("*", end=" ")
#                else:
#                    print(" ", end=' ')
#            print()
#
#    else:
#        print("try again")
#    keep = int(input("Press 1 for continue with the same color, 0 to close the program, CHANGE the color: 4 for red, 5 for green, 6 for yellow, 7 for blue  "))
#    if keep == 1:
#        continue
#    elif keep == 0:
#        break
#    elif keep == 4:
#        print(Fore.RED + '')
#    elif keep == 5:
#        print(Fore.GREEN + '')
#    elif keep == 6:
#        print(Fore.YELLOW + '')
#    elif keep == 7:
#        print(Fore.BLUE + '')