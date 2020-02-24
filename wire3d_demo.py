'''
=================
3D wireframe plot
=================

A very basic demonstration of a wireframe plot.

'''
#def CountParam(myroot,label):

    
import xml.etree.ElementTree as ET
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from tkinter import Tk
from tkinter import filedialog



root=Tk()
root.filename=filedialog.askopenfilename(title="File Open")
constants=[]
nodes=[]
elements=[]
material=[]
sections=[]
boundary=[]
loading=[]
mytree=ET.parse(root.filename)
myroot=mytree.getroot()

for x in myroot.findall('constants'):
   
    constants.append(x.text)
    print(x.tag,x.attrib)
    print(x.text)

for x in myroot.findall('nodes'):
    nodetag=x.tag
    nodeattrib=x.attrib
    print(x.tag,x.attrib)
    line = x.text.strip()
    lines=line.split('\n')
    nn=len(lines)
    i=0
    while i < nn:
        nodes.append(lines[i])
        print(lines[i])
        i +=1

        
for x in myroot.findall('elements'):
    elemtag=x.tag
    elemattrib=x.attrib
    print(x.tag,x.attrib)
    line = x.text.strip()
    lines=line.split('\n')
    ne=len(lines)
    i=0
    while i < ne:
        elements.append(lines[i])
        print(lines[i])
        i +=1
    
for x in myroot.findall('section'):
    sectag=x.tag
    secattrib=x.attrib
    print(x.tag,x.attrib)
    line = x.text.strip()
    lines=line.split('\n')
    nsec=len(lines)
    i=0
    while i < nsec:
        sections.append(lines[i])
        print(lines[i])
        i +=1         
for x in myroot.findall('material'):
    materialtag=x.tag
    materialattrib=x.attrib
    print(x.tag,x.attrib)
    line = x.text.strip()
    lines=line.split('\n')
    nmat=len(lines)
    i=0
    while i < nmat:
        material.append(lines[i])
        print(lines[i])
        i +=1            

for x in myroot.findall('boundary'):
    boundtag=x.tag
    boundattrib=x.attrib
    print(x.tag,x.attrib)
    line = x.text.strip()
    lines=line.split('\n')
    nbound=len(lines)
    i=0
    while i < nbound:
        boundary.append(lines[i])
        print(lines[i])
        i +=1        
for x in myroot.findall('loading'):
    case=x.find('case').text
    print(case)
    loadednodes=x.find('loadednodes')
    #loading.append(x.text)
    print(x.tag,x.attrib)
    print(loadednodes) 
    print(case)          
#print(myroot.tag)

''' for coor in nodes:
    print(coor)
for elem in elements:    
    print(elem)
for sect in sections:    
    print(sect)
for mat in material:
    print(mat)
for bound in boundary:    
    print(bound)
print(loading) '''

''' file1=open(root.filename,'r')
Lines=[]

count=0
with open(root.filename) as fp:
    Lines=fp.readlines()
    for line in Lines:
        #Lines.append(line)
        count +=1
        print("Line{}: {}".format(count,line.strip())) '''
    
#file1.close()    

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Grab some test data.
X, Y, Z = axes3d.get_test_data(0.05)

# Plot a basic wireframe.
ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10)

plt.show()
