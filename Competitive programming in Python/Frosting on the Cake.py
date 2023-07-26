def sum_by_class(l):
    return [sum(l[n :: 3]) for n in [0, 1, 2]]

def read_input():
    return [int(x) for x in input().split()]

vert = sum_by_class(read_input())
hor = sum_by_class(read_input())

print(hor[2]*vert[0] + hor[1]*vert[1] + hor[0]*vert[2], hor[0]*vert[0] + hor[1]*vert[2] + hor[2]*vert[1], hor[0]*vert[1] + hor[1]*vert[0] + hor[2]*vert[2])