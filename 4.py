
def is_palindrome(string):
    i = 0
    while i < len(string) / 2:
        if string[i] != string[-(i+1)]:
            return False
        i += 1
    return True

pal_list = []

for i in range(1, 999):
    for j in range(1, 999):
        result = i*j
        if is_palindrome(str(result)):
            pal_list.append(result)

largest = 0
for pal in pal_list:
    if pal > largest:
        largest = pal

print(largest)

