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

grpah = pydot.Dot(graph_type='digraph')
def genFixtures():
    random.shuffle(Teams)
    print(Teams)
    for i in Teams:
        grpah.add_node(pydot.Node(name=i))
    grpah.write_png('output.png')
genFixtures()


# for i in range(0,len(Teams),2):
#     print(i)
#     print(Teams[i:i+2])


def pair(list):
    temp=[]
    for i in range(0,len(list),2):
        #print(list[i:i+2])
        # for i in list[i:i+2]:
        temp.append(list[i:i+2])
    return temp

firstpair = pair(Teams)
print('first pair:',firstpair,'length: ',len(firstpair))

print()

# secondpair = pair(firstpair)
# print('second pair',secondpair,'length: ',len(secondpair))

# print()

# thirdpari = pair(secondpair)
# print('third pair',thirdpari,'length: ',len(thirdpari))

