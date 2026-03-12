num = int(input("Enter a number: "))
square = num * num

temp = num
count = 0

while temp > 0:
    count = count + 1
    temp = temp // 10

if square % (10 ** count) == num:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")