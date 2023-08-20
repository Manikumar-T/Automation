import pydot
import random
Teams=['Immortals',
'Workaholics',
'Wunderkinds',
'Alpha',
'Troubleshooters',
'Strikers',
'Vaporizers',
'Vigilantes',
'mani',

]

FixtureDict ={}
edgeDict={}
grpah = pydot.Dot(graph_type='graph',rankdir='LR')
Match_num =1

def pair(list,value):
    temp=[]
    print(value)
    for i in range(0,len(list),2):
        str1=''
        for j in list[i:i+2]:
            str1+=str(j).replace('vs','/')+" vs "

        edgeDict[tuple(list[i:i+2])]=str1.strip(' vs ')

        temp.append(str1.strip(' vs '))
    for j in temp :
             #grpah.add_node(pydot.Node(name=j))
             grpah.add_node(Match_num)
             Match_num+=1
    return temp

def genFixtureDict():
    dictTemp=Teams
    value=2
    FixtureDict[1]=Teams
    for j in Teams:
        grpah.add_node(pydot.Node(name=j,shape ='box'))

    while(len(dictTemp)!=1):
        dictTemp = pair(dictTemp,value)
        print('{} pair length: {}'.format(dictTemp,len(dictTemp)))
        FixtureDict[value] = dictTemp
        value+=1

    print(FixtureDict)
#def genEdge():
     
         
         

def genFixtures():
    
    random.shuffle(Teams)
    print(Teams)
    genFixtureDict()
    # for i in FixtureDict.keys():
    #     for j in FixtureDict[i]:
    #         grpah.add_node(pydot.Node(name=j))
  
       
    for i in edgeDict.keys():
        for j in i:
            if(j != edgeDict[i]):
                grpah.add_edge(pydot.Edge(j,edgeDict[i]))
             
    grpah.write_png('output.png')

genFixtures()


