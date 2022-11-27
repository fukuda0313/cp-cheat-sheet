"""素数判定法
入力された値が素数がどうか判定する
"""
# 整数を入力する
print("整数を入力してください")
N = int(input())

Answer = []
LIMIT = int(N**0.5)

# √N回判定する。
for i in range(2, LIMIT + 1):
    while N % i == 0:
        N /= i
        Answer.append(i)

if N >= 2:
    Answer.append(int(N))

# 出力
if len(Answer) == 1:
    print("素数です")
else:
    print("合成数です")

print(*Answer)
