import json
from bs4 import BeautifulSoup
import re
dict = {}
text = []
for i in range(2,306):
	try:
		soup = BeautifulSoup(open("poems/"+str(i)))
		# soup = BeautifulSoup(str(soup).replace(">&#160;", "\n&#160;"))
		# print soup.prettify()
		chapter = soup.find('h3').get_text()
		if(chapter==''):
			print i
		texts = ""
		for tags in soup.find_all('div','LOGLinegroup'):
			texts = texts + tags.get_text()+"<br>"
			if(tags.next_sibling.name=='br'):
				texts = texts + "<br>"
		text.append({'chapter':chapter,'text':texts})
	except:
		continue
poem = {'poem' : text}
f = open('leaves2.js', 'w')
f.write("var text = ")
f.write(json.dumps(poem))
# print text[25]['chapter']