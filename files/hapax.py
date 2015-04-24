import json
from bs4 import BeautifulSoup
import re
total=0
poems=0
dict = {}
soup = BeautifulSoup(open("1322-h.htm"))
for tags in soup.find_all('pre'):
	poems=poems+1
	l = re.compile("\W").split(tags.string)
	for l1 in l:
		total=total+1
		l2=l1.lower()
		if(l2!=""):
			if (dict.has_key(l2)):
				dict[l2]=dict[l2]+1
			else:
				dict[l2]=1
unique=0
hapax=0
hapaxwords = []
for d in dict:
	unique=unique+1
	if(dict[d]==1 and len(d)>2):
		hapax=hapax+1
		hapaxwords.append(str(d))

print 'total words='+str(total)
print 'unique words='+str(unique)
print 'hapax words='+str(hapax)
print 'total poems='+str(poems)
json1 = json.dumps(dict, ensure_ascii=False)
fo = open("leaveswords.js", "wb")
fo.write("var words = ")
fo.write(json1)
fo.write(";\n")
fo.write("var totalwords = ")
fo.write(str(total))
fo.write(";\n")
i=0
for w in sorted(dict, key=dict.get, reverse=True):
	# print w, dict[w]
	i=i+1
	if(i==60):
		break
fo.write("var hapax = ")
fo.write(str(hapaxwords))
fo.write(";\n")
# print 