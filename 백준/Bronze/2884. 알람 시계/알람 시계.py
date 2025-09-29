import sys

h, m = map(int, sys.stdin.readline().split())

# m >= 45 이면 그냥 뺌
if m >= 45:
    m = m - 45
    print(h, m)
# m < 45 이면 h-1 하고 (m + 60) - 45
else:
    ## h-1 < 0 이면 (h + 24) - 1
    if (h-1) < 0 :
        h = (h+24)-1
        m = (m+60)-45
        print(h, m)
    else:
        h = h-1
        m = (m+60)-45
        print(h, m)
