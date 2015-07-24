"""
runtime: 0.001 seconds

Made a function to generate the string version of numbers (in words), called
for every number and adding together using len(). I think there are easy ways
to do this. You don't need to form the words, you could just use numbers, but I
thought it would be cooler to have the function return strings. It also made it
super easy to debug by dumping all the strings into an empty file and comparing
them to the line number.
"""

import time

u20 = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight',
       'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen',
       'sixteen', 'seventeen', 'eighteen', 'nineteen']

tens_list = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy',
        'eighty', 'ninety']

def num_to_text(num):
    ones = int(num % 10)
    tens = int((num % 100)/10)
    hund = int((num % 1000)/100)
    
    text = ''

    if hund != 0:
        text += u20[hund] + 'hundred'
        if tens != 0 or ones != 0:
            text += 'and'
    if tens == 0 or tens == 1:
        text += u20[tens*10+ones]
    else:
        text += tens_list[tens]
        if ones != 0:
            text += u20[ones]
    if num == 1000:
        text = 'onethousand'
    return text
        
# num_to_text - End #

# Main #
start = time.time()

total = 0
for i in range(1, 1001):
    total += len(num_to_text(i))

end = time.time()
print('total:', total)
print(' time:', end-start, 'seconds')

# Main - End #
