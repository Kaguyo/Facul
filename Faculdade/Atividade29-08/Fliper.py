p, r = map(int, input().split())

while (p != 0 and p != 1) or (r != 0 and r != 1):
    p, r = map(int, input().split())

if p == 0:
    print('C')
elif p == 1 and r == 0:
    print('B')
else:
    print('A')