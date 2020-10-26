# Keyboard
rand_keyboard = open('random3.txt','w')

keyboard = 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm'

text_length = 10000
line_length = 15

index = 0
output = ''
for i in range(text_length):
	for j in range(line_length):
		index %= len(keyboard)
		output += keyboard[index]
		index += 1
	output += '\n'
	
rand_keyboard.write(output)
