N, M = map(int, input().split(" "))

ac_flag = [0 for _ in range(N)]
wa = ac_flag.copy()

for i in range(M):

    question, result = input().split(" ")
    question = int(question)

    if not ac_flag[question-1] and result == 'WA':
        wa[question - 1] += 1
    
    if result == 'AC':
        ac_flag[question-1] = 1

wa = [x*y for x, y in zip(ac_flag, wa)]
print(sum(ac_flag), sum(x*y for x, y in zip(wa, ac_flag)))