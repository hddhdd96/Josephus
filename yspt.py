import sys

N, K = map(int, sys.stdin.readline().split(' '))

circular_list = [ i for i in range(1, N+1)]

answer = []
pop_num = 0

while len(circular_list) != 0:
    pop_num = (pop_num + (K-1)) % len(circular_list)
    answer.append(str(circular_list.pop(pop_num)))

print("<%s>" % (", ".join(answer)))
