# Symbol
symbol_out = open('random6.txt','w')

symbol = '!@#$%^&*()-+{}|:"<>?[]\;\',./'

line_length = 20
text_length = 20000
output = ''
index = 0

for i in range(text_length) :               
	for j in range(line_length) : 
		index %= len(symbol)
		output += symbol[index]              
		index += 1       
	output += '\n'
	
symbol_out.write(output)
