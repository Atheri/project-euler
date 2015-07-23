"""
runtime: 0.002 seconds

Tried to do a recursive brute force of all possible paths, but after letting it
run for 5 min it was going to take too long. So I went back to the idea from
the last problem, if I can build the bigger problem ontop of smaller problems,
I can keep track of the smaller ones so I don't have to compute them again. So
as it relates to this problem, I store a grid of numbers that represent how
many routes to end are possible from that point in the grid. Since you can only
go right and down, any point in the grid can be calculated by adding together
it's right and down adjacent point. So if I start in the bottom right corner,
and go backwards to the start point, I can calculate the number of routes
(which kind of looks like a pascal's triangle).

After finishing this one I found a lot of references to this as a dynamic
programming solution, never really heard of that, I'll have to look into it.
"""


import time

# Main #
start = time.time()

n = 20
routes = 0

# Create a (n+1) square matrix, filled with 0 except for the last row and
# column which is filled with ones. To me this is pretty unreadable, but I was
# looking into list comprehension, so I gave it a go.
grid = [[0 if x != n else 1 for x in range(0,n+1)] if x != n else [1]*(n+1) for x in range(0,n+1)]

# Could make the same grid with
"""
grid = [[0]*n for x in range(0,n)] # n sqaure matrix of 0's
for x in grid: x.append(1)         # append a 1 to each row
grid.append([1]*(n+1))             # add the row of all 1's
"""

for i in range(n-1, -1, -1):
    for j in range(n-1, -1, -1):
        grid[i][j] = grid[i+1][j] + grid[i][j+1] 

        
routes = grid[0][0]
print("routes", routes)
end = time.time()
print("time:", end-start, "seconds")
# Main - End #




