
cards = [int(i) for i in input().split(" ")]
print("bust" if sum(cards) >= 22 else "win")