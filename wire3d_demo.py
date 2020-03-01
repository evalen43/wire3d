'''
=================
3D wireframe plot
=================

A very basic demonstration of a wireframe plot.

'''
#def CountParam(myroot,label):

    
import xml.etree.ElementTree as ET
import mpl_toolkits.mplot3d as plot3d
import matplotlib.pyplot as plt
from tkinter import Tk, Canvas, Frame, BOTH
from tkinter import filedialog
from matplotlib.collections import LineCollection
import numpy as np
class Example(Frame):
    
    def __init__(self):
        super().__init__()

        self.initUI()
        self.drawLines(x,y,incidence,ne)


    def initUI(self):

        self.master.title("Lines")
        self.pack(fill=BOTH, expand=1)

        canvas = Canvas(self)
        canvas.create_line(15, 25, 200, 25)
        canvas.create_line(300, 35, 300, 200, dash=(4, 2))
        canvas.create_line(55, 85, 155, 85, 105, 180, 55, 85)

        canvas.pack(fill=BOTH, expand=1)
        
    def drawLines(self,x,y,incidence,ne) :
        self.x=x
        self.y=y
        self.incidence=incidence
        self.ne=ne
        canvas=Canvas(self)  
        i=0
        while i < self.ne :
            
            canvas.create_line(self.x[self.incidence[i][0]],self.y[self.incidence[i][0]],self.x[self.incidence[i][1]],self.y[self.incidence[i][1]])
            i +=1
        canvas.pack(fill=BOTH, expand=1)    
         

#def main():
root=Tk()

root.filename=filedialog.askopenfilename(title="File Open")
root.geometry("400x250+300+300")
    #root.mainloop()

#if __name__ == '__main__':
 #   main()
    



constants=[]
nodes=[]
elements=[]
material=[]
sections=[]
boundary=[]
loading=[]
jnload=[]

mytree=ET.parse(root.filename)
myroot=mytree.getroot()

#for child in myroot:
    #print(child.tag,child.attrib)

for x in myroot.findall('constants'):
   
    constants.append(x.text)
    #print(x.tag,x.attrib)
    #print(x.text)

for x in myroot.findall('nodes'):
    nodetag=x.tag
    nodeattrib=x.attrib
    #print(x.tag,x.attrib)
    line = x.text.strip()
    lines=line.split('\n')
    nn=len(lines)
    i=0
    while i < nn:
        nodes.append(lines[i])
        #print(lines[i])
        i +=1

        
for x in myroot.findall('elements'):
    elemtag=x.tag
    elemattrib=x.attrib
    #print(x.tag,x.attrib)
    line = x.text.strip()
    lines=line.split('\n')
    ne=len(lines)
    i=0
    while i < ne:
        elements.append(lines[i])
        #print(lines[i])
        i +=1
    
for x in myroot.findall('section'):
    sectag=x.tag
    secattrib=x.attrib
    #print(x.tag,x.attrib)
    line = x.text.strip()
    lines=line.split('\n')
    nsec=len(lines)
    i=0
    while i < nsec:
        sections.append(lines[i])
        #print(lines[i])
        i +=1         
for x in myroot.findall('material'):
    materialtag=x.tag
    materialattrib=x.attrib
    #print(x.tag,x.attrib)
    line = x.text.strip()
    lines=line.split('\n')
    nmat=len(lines)
    i=0
    while i < nmat:
        material.append(lines[i])
        #print(lines[i])
        i +=1            

for x in myroot.findall('boundary'):
    boundtag=x.tag
    boundattrib=x.attrib
    #print(x.tag,x.attrib)
    line = x.text.strip()
    lines=line.split('\n')
    nbound=len(lines)
    i=0
    while i < nbound:
        boundary.append(lines[i])
        #print(lines[i])
        i +=1        


    
i=0
line=[]
nodeid=[None]*nn
elemid=[None]*ne
x=np.empty(nn,dtype=float)
y=np.empty(nn, dtype=float)
z=np.empty(nn, dtype=float)
while i < nn  :
    line= nodes[i].split() 
    num=len(line)
      
    nodeid[i]=line[0]
    if num >0 :
        x[i]=float(line[1])
    if num > 1 :    
        y[i]=float(line[2])
    i +=1 
#print(nodeid,x,y) 
incidence=np.arange(ne*2).reshape(ne,2)
i=0
while i<ne :
    line= elements[i].split() 
    num=len(line)
      
    elemid[i]=line[0]
    if num >0 :
        result=nodeid.index(line[1])
        #print(result)
        incidence[i][0]=int(nodeid.index(line[1]))
        incidence[i][1]=int(nodeid.index(line[2]))
        i +=1  
#print(incidence)

fig = plt.figure()
fig.set_size_inches(10,10)
ax = fig.add_subplot(111, projection='3d')#, aspect='equal')
ax.view_init(azim=120)
#X, Y, Z = axes3d.get_test_data(0.05)

# Plot a basic wireframe.

ax.scatter3D(x, y, z,color='black', marker='s') #, c=np.array(zz), cmap='Greens') #,rstride=10, cstride=10)
for i in range(ne):
    xs=x[incidence[i][0]],x[incidence[i][1]]
    ys=y[incidence[i][0]],y[incidence[i][1]]
    zs= 0.0, 0.0
    line=plot3d.art3d.Line3D(xs,ys,zs)
    ax.add_line(line)

ex = Example()
ex.drawLines(x,y,incidence,ne)

plt.show()


