# Lipsum
lipsum_file = open('lipsum-src.txt','r')
lipsum_out = open('random2.txt','w')
lipsum = lipsum_file.read()

line_length = 10
text_length = 10000
output = ''
index = 0

for char in lipsum : 
    if(char.isalpha() == True):
        output += char
    if(len(output) %line_length == 0):
        output += '\n'

lipsum_out.write(output)

