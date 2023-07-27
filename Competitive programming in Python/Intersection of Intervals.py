def intersect_max(set):
    l = ([(left, +1) for left, _ in set] 
         + [(right + 1, -1) for _, right in set]) # +1 to get an interval closed
                                                # on the right, it matches the prologin
                                                #  challenge and not the book
    l.sort()
    counter = 0
    opti = (counter, None)
    for (x, y) in l:
        counter += y
        if opti[0] < counter:
            opti = (counter, x)
    return opti


n = int(input())
set = []
for i in range(n):
    start, end = [int(year) for year in input().split()]
    set.append((start, end))


print(intersect_max(set)[0])