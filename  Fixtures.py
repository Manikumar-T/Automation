import pydot
import random
Teams=['Immortals',
'Workaholics',
'Wunderkinds',
'Alpha',
'Troubleshooters',
'Strikers',
'Vaporizers',
'Vigilantes','mani']

FixtureDict ={}

def pair(list):
    temp=[]
    for i in range(0,len(list),2):
        str1=''
        #print(list[i:i+2])
        for i in list[i:i+2]:

            str1+=str(i).replace('vs','/')+" vs "
        temp.append(str1.strip(' vs '))
    return temp

def genFixtureDict():
    dictTemp=Teams
    value=2
    FixtureDict[1]=Teams
    while(len(dictTemp)!=1):
        dictTemp = pair(dictTemp)
        print('{} pair length: {}'.format(dictTemp,len(dictTemp)))
        FixtureDict[value] = dictTemp
        value+=1

    print(FixtureDict)

grpah = pydot.Dot(graph_type='digraph')
def genFixtures():
    
    random.shuffle(Teams)
    print(Teams)
    genFixtureDict()
    for i in FixtureDict.keys():
        for j in FixtureDict[i]:
            grpah.add_node(pydot.Node(name=j))
  
            

    grpah.write_png('output.png')
genFixtures()


