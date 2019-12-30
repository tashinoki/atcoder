
def validation(i):

    if i == 0 or i == 1:
        return i

    else:
        return 0

square = map(validation, [int(i) for i in input().strip()])

print(list(square).count(1))