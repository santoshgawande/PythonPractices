def chekstring(str1):
	if str1.isalnum() :
		print(True)
	else:
		print(False)
	
	for ch in str1:
		if ch.isalpha():
			print(True)
			break
	else:
		print(False)
	
	for ch in str1:
		if ch.isdigit():
			print(True)
			break
	else:
		print(False)
		
	for ch in str1:
		if ch.islower():
			print(True)
			break
	else:
		print(True)
	
	for ch in str1:
		if ch.isupper():
			print(True)
			break
	else:
		print(False)
		
if '__name__' == '__main__':
	s = input()
	chekstring('qA2')