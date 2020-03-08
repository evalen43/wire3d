'''
=================
3D wireframe plot
================='''
    
import xml.etree.ElementTree as ET
import mpl_toolkits.mplot3d as plot3d
import matplotlib.pyplot as plt
from tkinter import ttk
from tkinter import *
from tkinter import filedialog
from matplotlib.collections import LineCollection
import numpy as np
import re
import threading
#import wire3d_mod as wiremod

class Application(Frame):
    
    def _init_(self,root):
        self.root=root

               
        
        
        
    def initUI(self,root):
        self.root=root
        self.root.columnconfigure(0,weight=2)
        self.root.rowconfigure(0,weight=2)         
        mainframe=ttk.Frame(self.root, borderwidth=5, width=200,height=100,padding="3 3 22 22")
        mainframe.grid(column=0,row=0,sticky=(N,W,E,S))
        ttk.Button(mainframe,text="Open File",command=self.openfile),mainframe.grid(column=3,row=3,sticky=W)
        self.root.state("zoomed")
        for child in mainframe.winfo_children():
            child.grid(padx=5,pady=5)
        self.root.bind('<Return>',self.openfile(root))
        self.root.geometry("400x250+300+300") 
           
    def openfile(self,root):
        self.root=root
        self.root.filename=filedialog.askopenfilename(title="File Open")
        return self.root.filename        

if __name__ == '__main__':
 
    root=Tk()
    root.title("Wire3D")
    app=Application(root)
    app.initUI(root)
    root.filename=app.openfile(root)
    mytree=ET.parse(root.filename)
    myroot=mytree.getroot()
    print(myroot.tag,myroot.attrib)

    for child in myroot:
        print(child.tag,child.attrib) 
    root.mainloop()
    
    



constants=[]
nodes=[]
elements=[]
material=[]
sections=[]
boundary=[]
loading=[]
jnload=[]




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
fig.set_size_inches(9.5,9.5)
ax = fig.add_subplot(111, projection='3d')#, aspect='equal')
ax.view_init(azim=120)
ax.set_xlabel('X Coordinate')
ax.set_ylabel('Y Coordinate')
ax.set_zlabel('Z Coordinate')
#X, Y, Z = axes3d.get_test_data(0.05)

# Plot a basic wireframe.

ax.scatter3D(x, y, z,color='black', marker='s') #, c=np.array(zz), cmap='Greens') #,rstride=10, cstride=10)
for i in range(ne):
    xs=x[incidence[i][0]],x[incidence[i][1]]
    if myroot.tag=='Frame2D' :
        #print('Frame2D')
        ys=y[incidence[i][0]],y[incidence[i][1]]
        zs= 0.0, 0.0
    line=plot3d.art3d.Line3D(xs,ys,zs)
    ax.add_line(line)

#ex = wiremod.Example(root,x,y,incidence,ne)
#ex.drawLines()

plt.show()


