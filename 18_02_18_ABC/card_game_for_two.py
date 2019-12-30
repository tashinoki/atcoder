
N = int(input())

cards = [data for i, data in enumerate(sorted(map(int, input().split(" ")), reverse=True))]
print(sum(cards[0::2]) - sum(cards[1::2]))