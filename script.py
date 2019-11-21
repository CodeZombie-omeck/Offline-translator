from translate import Translator

translator= Translator(to_lang="pt")
try:
	with open ('./test.txt', mode = 'r') as file:
		text = file.read()
		translation = translator.translate(text)
		with open ('./transtest.txt', mode = 'w') as file2:
			file2.write(translation)
except TabError as c:
	print('check your spaces')
	
	
	

	
 







