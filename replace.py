import sys
import csv
from os import path
from docx import Document
#Get the command line argv 
options = sys.argv[1:]
optionDict={
    "-f":"none",
    "-r":"none",
    "-rf":"none",
    "-doc":"none"        
            }
replace_text =[]
find_text=[]
#Read the file
def reacsv(text_path): 
    with open(text_path,'r') as f:
        text =list(csv.reader(f,delimiter=','))
        print('Reading Text File...')
        j=0
        print('filtering data...')
        for i in text:
            if(len(i)>0 and len(text[0])==len(i) and len(find_text)==len(text[0])):
                replace_text.append(i)
                j+=1
            else:
                print('Data Filtering Faild at line no :',j)
                j+=1
            
            
              

def replaceText(doc_path):
    for sub in replace_text:
        print(sub)
        doc = Document(doc_path)
        for p in doc.paragraphs:
            for index in range(len(find_text)):
                p.text=p.text.replace(find_text[index],sub[index])
                print(p.text)
        doc.save('./doc/'+sub[0]+".docx")

def optionFilter():
    for i in range(len(options)):
        #filter the Find string arg
        if(options[i]=='-f'):
            optionDict['-f']=options[i+1].split(',')
        elif('-f' not in options):
            print('find  option compulsory')
            exit(0)
        
        #filter the replace single arg
        if(options[i]=='-r' and '-rf' not in options):
                optionDict['-r'] = options[i+1].split(',')
        elif('-r' in options and '-rf'in options):
            print('-f and -rf are same option')
            exit(0)
        elif('-r' not in options and '-rf'not in options):
            print('replace option compulsory')
            exit(0)

        #filter the replace multi file path arg
        if(options[i]=='-rf' and '-r' not in options):
                if(path.isfile(options[i+1])):
                    optionDict['-rf'] = 'F'+options[i+1]
                else:
                    print('replace text file not found')

        elif('-r' in options and '-rf'in options):
            print('-f and -rf are same option')
            exit(0)

        elif('-r' not in options and '-rf'not in options):
            print('replace option compulsory')
            exit(0)
        #filter the doc file arg
        #filter the replace multi file path arg
        if(options[i]=='-doc'):
                if(path.isfile(options[i+1])):
                    optionDict['-doc'] = options[i+1]
                else:
                    print('doc file not found')

        elif('-doc' not in options):
            print('document option compulsory')
            exit(0)

def funCaller():
    optionFilter()
    if(optionDict['-f']!='none' and optionDict['-r'] !='none'):
        replace_text=optionDict['-r']
        find_text=optionDict['-f']
        replaceText()
        
funCaller()
print("The replace text ",replace_text)
print("The find text ",find_text)
print("Option filtered ",optionDict)

    