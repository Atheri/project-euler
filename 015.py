
import time

def choose_path(x, y):
    if x == grid_size and y == grid_size:
        return 1
    elif x > grid_size or y > grid_size:
        return 0

    return choose_path(x+1, y) + choose_path(x, y+1) 

# choose_path - End #

def calc_routes(x, y):
    if x >= grid_size and y >= grid_size:
        return 0
    return choose_path(x, y)

# calc_routes - End #

# Main #
start = time.time()

grid_size = 20
routes = calc_routes(0, 0)



print("routes", routes)
end = time.time()
print("time:", end-start, "seconds")
# Main - End #




