
a, b =[int(i) for i in input().strip().split(" ")]

if (a * b) % 2 == 0:
    print("Even")

else:
    print("Odd")