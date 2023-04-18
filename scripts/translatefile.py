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
	name="chapters/1.txt"
	newst=""
	txt=readfilestr(name).replace("\n","").replace(".","\n")
	maxsize=4999
	print(len(txt)/maxsize)
	k=len(txt)/maxsize
	#for i in range(len(a)/5000):
	i=0	
	while True:
		try:
			if(math.floor(k)/maxsize<=i):
				txt=webTranslate(txt[i*maxsize:(i*maxsize)+i%maxsize],"en","pt")
			else:
				txt=webTranslate(txt[i*maxsize:(i+1)*maxsize],"en","pt")
			#if(math.floor(k)+1<i): break
			
		except:
			break
		print(txt)
		i+=1
	writetxt(name.replace(".","portugese."),txt)#"".join(a))
main()
