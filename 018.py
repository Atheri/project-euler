"""
runtime: 8.606910705566406e-05 seconds

In the problem description, they warned that this could easily be naively brute
forced, but down the road there would be the same problem with a much larger
set. So I attempted a dynamic solution where I traverse the tree top down, and
calculate the longest path for each cell in that row by looking at the greater
of cell's parents. This populates the tree in a single pass, and then you just
find the max of the last row to find the greatest path. Reminds me of shortest
path algorithms.

I'm not sure if it will be sufficient for the longer problem, we'll see.
"""

import time

init = []
init.append('75                                          ')
init.append('95 64                                       ')
init.append('17 47 82                                    ')
init.append('18 35 87 10                                 ')
init.append('20 04 82 47 65                              ')
init.append('19 01 23 75 03 34                           ')
init.append('88 02 77 73 07 63 67                        ')
init.append('99 65 04 28 06 16 70 92                     ')
init.append('41 41 26 56 83 40 80 70 33                  ')
init.append('41 48 72 33 47 32 37 16 94 29               ')
init.append('53 71 44 65 25 43 91 52 97 51 14            ')
init.append('70 11 33 28 77 73 17 78 39 68 17 57         ')
init.append('91 71 52 38 17 14 91 43 58 50 27 29 48      ')
init.append('63 66 04 68 89 53 67 30 73 16 69 87 40 31   ')
init.append('04 62 98 27 23 09 70 98 73 93 38 53 60 04 23')

n = len(init)

a = []
b = []
for string in init:
    a_row = []
    b_row = []
    for num in string.split():
        a_row.append(int(num))
        b_row.append(0)
    a.append(a_row)
    b.append(b_row)

start = time.time()

for row in range(0,n):
    for col in range(0,len(a[row])):
        if row == 0 and col == 0: 
            b[row][col] = a[row][col]
        elif col == 0: 
            b[row][col] = a[row][col] + b[row-1][col]
        elif col == len(a[row])-1: 
            b[row][col] = a[row][col] + b[row-1][col-1]
        else:
            if b[row-1][col] > b[row-1][col-1]:
                b[row][col] = a[row][col] + b[row-1][col]
            else:
                b[row][col] = a[row][col] + b[row-1][col-1]

result = max(b[n-1])

end = time.time()
print('result:', result)
print('  time:', end-start, 'seconds')
