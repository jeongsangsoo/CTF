import dis
import binascii 

f= open("./encodedflag.txt","rb")

def C2(inpString):
	xorKey = 'S'
	length = len(inpString)
	for i in range(length):
		inpString = inpString[:i]+chr(ord(inpString[i])^ord(xorKey))+inpString[i+1:]
	return inpString

def reverse_C2(inpString):
    xorKey = "S"
    result = ''
    for i in range(len(inpString)):
        result+= chr(ord(inpString[i])^ord(xorKey))
    st = ''
    for i in range(len(result)-1,-1,-1):
        st+=result[i]
    return st

def C1(text):
	ret_text = ''
	for i in list(text):
		counter = text.count(i)
		ret_text += chr(2*ord(i)-len(text))
	return ret_text

def reverseC1(text):
    ret_text= ''
    for i in text:
        ret_text+= chr(int((ord(i)+len(text))/2))
    return ret_text

#print(dis.dis(C1))
print(dis.dis(C2))
enc_data = f.read()
#print(f'{enc_data}')
print(reverseC1(str(reverse_C2(str(enc_data)))))


