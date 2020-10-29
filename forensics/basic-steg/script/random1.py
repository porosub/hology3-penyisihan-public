# Angka
rand_num = open('random1.txt','w')

number =  '1234567890'

text_length = 5000
line_length = 8

output = ''
index = 0
for i in range(text_length):
    index %= len(number)
    for j in range(line_length):
        if(index == len(number)):
            index = 0
        output += number[index]
        index += 1
        line_length -= 1
    line_length = 8
    output += '\n'

rand_num.write(output)

