cards = int(input())
seq = [int(i) for i in input().split()]
win_seq = [int(i) for i in input().split()]

answer = 'NO'

for i in range(cards):
    if  seq[i] == win_seq[i]:
        continue
    for j in range(i+1, cards):
        sorted_seq = sorted(seq[i:j+1])
        check_seq = seq[:i] + sorted_seq + seq[j+1:]
        if check_seq == win_seq:
            answer = 'YES'

print(answer)
