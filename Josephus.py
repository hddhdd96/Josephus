# https://level.goorm.io/exam/43266/%ED%99%A9%EC%A0%9C%EC%9D%98-%EB%AA%B0%EB%9D%BD/quiz/1

import sys

N, K = map(int, sys.stdin.readline().split(' '))

poro = [i for i in range(N)]

temp = 0

while len(poro) != 2:
    del poro[temp]

    temp = (temp + (K - 1)) % len(poro)

print(poro[0] + 1, poro[1] + 1)



