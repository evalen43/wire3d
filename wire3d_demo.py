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
    sections.append(x.text)
    print(x.tag,x.attrib)
    print(x.text)          
for x in myroot.findall('material'):
    material.append(x.text)
    print(x.tag,x.attrib)
    print(x.text)    

for x in myroot.findall('boundary'):
    boundary.append(x.text)
    print(x.tag,x.attrib)
    print(x.text)    
for x in myroot.findall('loading'):
    loading.append(x.text)
    print(x.tag,x.attrib)
    print(x.text)           
#print(myroot.tag)

for coor in nodes:
    
    print(coor)
print(elements)
print(sections)
print(material)
print(boundary)
print(loading)

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
