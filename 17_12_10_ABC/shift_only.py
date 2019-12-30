
N = int(input().strip())

numbers = [int(i) for i in input().strip().split(" ")]

if len(numbers) != N:
    print("invalid input data")
    exit

count = 0

def is_all_even(arr):

    for i in arr:

        if i % 2 == 1:
            return False
    
    return True

while(is_all_even(numbers)):

    numbers = [ i // 2 for i in numbers]
    count += 1

print(count)