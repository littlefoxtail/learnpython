import re
frworigin = open('font2.txt', 'r', encoding="utf-8")
text = frworigin.read()

frwoutput = open('output.txt', 'w', encoding='utf-8')
newtext = re.sub('[\s+]', '', text)
print(newtext)
frwoutput.write(newtext)
frworigin.close
frwoutput.close