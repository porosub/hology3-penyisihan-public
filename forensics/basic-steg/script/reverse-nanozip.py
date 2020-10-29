# Reverse tiap byte nanozip
import binascii

with open('real.nz','rb') as f : 
	hexdata = f.read().hex()

hexrev = [hexdata[i:i+2] for i in range(0,len(hexdata),2)]

hexfinalrev = hexrev[::-1]

with open('rev.nz','wb') as ff:
	ff.write(binascii.unhexlify("".join(hexfinalrev)))
