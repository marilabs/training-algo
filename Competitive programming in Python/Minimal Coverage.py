M = int(input())
set = []

while input() != '0 0':
    start, end = [int(number) for number in input().split()]
    set.append((start, end))

def minimal_coverage(set):
    setbis = sorted(set)
    if setbis[0] > M or setbis[-1] < M:
        return 'No solution'
    else:
        n = len(setbis)
        return 'not done'