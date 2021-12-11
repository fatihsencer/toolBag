def printOrd(text):
	for x in text:
		print("| {:03} |\t".format(ord(x)),end='')

	print('\n')

def printText(text):
	for x in text:
		print("|  {}  |\t".format(x),end='')

	print('\n')

flag = input('1- crypted and encrypted\n2- Just crypted\n: ')


if flag == '1':

	cryptedText = input('Crypted Text: ').replace(" ", "")
	encryptedText = input('Encrypted Text: ').replace(" ", "")

	print('-'*len(cryptedText)*8,end='\n\n')

	printText(cryptedText)

	printOrd(cryptedText)

	print('-'*len(cryptedText)*8,end='\n\n')

	printText(encryptedText)

	printOrd(encryptedText)

	print('-'*len(cryptedText)*8,end='\n\n')

	for (x,y) in zip(cryptedText,encryptedText):
		print("| {:03} |\t".format(ord(x)-ord(y)),end='')


else :
	cryptedText = input('\n\nCrypted Text: ').replace(" ", "")

	print('-'*len(cryptedText)*8,end='\n\n')

	printText(cryptedText)

	printOrd(cryptedText)