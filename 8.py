adj_num = 13

input = []

# This was easiest to copy and paste
input.append("73167176531330624919225119674426574742355349194934")
input.append("96983520312774506326239578318016984801869478851843")
input.append("85861560789112949495459501737958331952853208805511")
input.append("12540698747158523863050715693290963295227443043557")
input.append("66896648950445244523161731856403098711121722383113")
input.append("62229893423380308135336276614282806444486645238749")
input.append("30358907296290491560440772390713810515859307960866")
input.append("70172427121883998797908792274921901699720888093776")
input.append("65727333001053367881220235421809751254540594752243")
input.append("52584907711670556013604839586446706324415722155397")
input.append("53697817977846174064955149290862569321978468622482")
input.append("83972241375657056057490261407972968652414535100474")
input.append("82166370484403199890008895243450658541227588666881")
input.append("16427171479924442928230863465674813919123162824586")
input.append("17866458359124566529476545682848912883142607690042")
input.append("24219022671055626321111109370544217506941658960408")
input.append("07198403850962455444362981230987879927244284909188")
input.append("84580156166097919133875499200524063689912560717606")
input.append("05886116467109405077541002256983155200055935729725")
input.append("71636269561882670428252483600823257530420752963450")

char_list = []

for i in input:
    for c in list(i):
        char_list.append(c)

print(range(len(char_list)-adj_num))
print(range(adj_num))

largest = 0
cur_num = 1

for i in range(len(char_list)-adj_num):
    for j in range(adj_num):
        cur_num = cur_num * int(char_list[i+j])
    if cur_num > largest:
        largest = cur_num
    cur_num = 1

print(largest)
