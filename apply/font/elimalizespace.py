import re

with open('font2.txt', 'r', encoding="utf-8") as frworigin:
    with open('output.txt', 'w', encoding='utf-8') as frwoutput:
        for originline in frworigin:
            newtext = re.sub('[\s+]', '', originline)
            print(newtext)
            frwoutput.write(newtext)


