import time

start = time.time()

f = open('p022_names.txt', 'r')
names = f.read().replace('"', '').split(',')

f.close()

print(names)
end = time.time()
print("time:", end-start, "seconds")
