import math
def readfilestr(name):
	"""
	readtxtstr(name) , return txt content as string
	"""
	content = ""
	with open(name, 'r') as file:
		for i in file.readlines():
			content += str(i)
	return content
def readfilelist(name):
	"""
	readtxt(name) , return txt content as array ,element by line 
	"""
	content = []
	with open(name, 'r') as file:
		for i in file.readlines():
			content.append(str(i).replace("\n",""))
	return content
def writetxt(name,content):
	"""
	writetxt(name,content) , write in txt file something  
	"""
	content =str(content)
	with open(name, 'w') as file:
		file.write(content)
		file.close()

def webTranslate(txt,writeIn,translateTo):
	"""
	webTranslate(txt,writeIn,translateTo )
	  - txt			  -text to trasnlate
	  - writeIn		  -in which language is it written
	  - translateTo	  -language to be translated
	rember language prefix
	en -> english
	es -> spanish 
	pt -> portugese 
	...
	"""
	from deep_translator import GoogleTranslator 
	translatedTxt = GoogleTranslator(source=writeIn, target=translateTo).translate(txt)
	return translatedTxt
def main():
	name="chapters/9.txt"
	txt=readfilelist(name)
	newtxt=""
	translated="portugese."
	for i in txt:
		try:
			newtxt+=webTranslate(i,"en","pt")+"\n"
			print(newtxt)
		except:
			writetxt(name.replace(".",translated),newtxt)#"".join(a))
			exit()
	writetxt(name.replace(".",translated),newtxt)#"".join(a))
def main2():
	name="chapters/10.txt"
	a=readfilestr(name).replace("\n","").replace(".","\n")
	print(a)
	writetxt("chapters/10new.txt",a)

main()
