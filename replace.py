import sys
import csv
from docx import Document
#Get the command line argv 
arg = sys.argv[1:]

print(arg)
replace_text =[]
#Read the file 
with open("data.txt",'r') as f:
    text =list(csv.reader(f,delimiter=','))
    print('Reading Text File...')
    j=0
    print('filtering data...')
    for i in text:
        if(len(i)>0 and len(text[0])==len(i)):
            replace_text.append(i)
            j+=1
        else:
            print('Data Filtering Faild at line no :',j)
            j+=1
            
            
              
print(replace_text)

for sub in replace_text:
    print(sub)
    doc = Document('Ex3_vigenerecipher.docx')
    for p in doc.paragraphs:
        for index in range(len(arg)):
            p.text=p.text.replace(arg[index],sub[index])
            print(p.text)
    doc.save('./doc/'+sub[0]+".docx")
      
         

            

    