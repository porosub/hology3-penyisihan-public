# Alfabet
rand_file = open('random4.txt','w')

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

line_length = 15
text_length = 15000
output = ''
index = 0


for i in range(text_length) :               
	for j in range(line_length) : 
		index %= len(alpha)
		output += alpha[index]              
		index += 1       
	output += '\n'
rand_file.write(output)
