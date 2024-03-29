import wx
from tokenize import tokenize, untokenize, NUMBER, STRING, NAME, OP
from io import BytesIO
import wx.xml
#import wx.dataview

g=9.806
ndf=0
lineinput = []
fyield=0.0
def TokNperM2(unitF):
    if unitF == "kN/m2":
        tonewton=1.0
    elif unitF =="lb/sqf":
        tonewton = 0.047880258888889
    elif unitF=="ksi":
        tonewton = 6894.757280000001
    elif unitF=="kgf/m2":
        tonewton=g
    elif unitF=="ton/sqf":
        tonewton = 107.25177991111
    elif unitF=="psi":
        tonewton = 6.89475728
    else:
        tonewton=1.0
    return tonewton        
        
def TokNperM3(unitF):
    if unitF=="kN/m3":
        tonewton=1.0
    elif unitF=="lbf/ft3":
        tonewton = 0.1570865731
    elif unitF=="kips/inch3":
        tonewton = 271447.14116097
    elif unitF=="kgf/m3":
        tonewton=g/1000.0
    elif unitF=="tonf/ft3":
        tonewton = 314.1731461238
    elif unitF=="t/m3":
        tonewton=g
    else:
        tonewton=1.0
    return tonewton            

def XML_reader(filein):
    # start processing the XML file
    doc = wx.xml.XmlDocument()
    if not doc.Load(filein):
        return False

    strutype = doc.GetRoot().GetName()
    if strutype =="Frame2D":   ndf=3
    elif strutype =="Frame3D": ndf=6
    elif strutype =="Truss3D": ndf=3
    elif strutype =="Truss2D": ndf=2
    elif strutype =="Grid":    ndf=3
    elif strutype =="Frame2D_8DOF": ndf=4
    else: ndf=3    
    #print(strutype)

    #     if child.GetType() == wx.xml.XML_PI_NODE and child.GetName() == "target":

    #         # process Process Instruction contents
    #         pi = child.GetContent()

            # Other code here...
    child = doc.GetRoot().GetChildren()
    while child:
        tagname = child.GetName()
        content = child.GetNodeContent()  # process text enclosed by tag1/tag1
        scaleS = 0.0

        if tagname == "title":
            projName=content
            # # process attributes of tag1
            # attrvalue1 = child.GetAttribute("attr1", "default-value")
            #attrvalue2 = child.GetAttribute("attr2", "default-value")
        elif tagname == "code":
            UnitS = child.GetAttribute("unitS", "kN/m2")  # UnitS: stress unit ...
            print(UnitS)
            if UnitS == "default-value": scaleS=1.0
            else: scaleS=TokNperM2(UnitS)                    
            content=content.replace("="," ")
            content=content.replace("\n"," ")
            lineinput=content.split()
            print(lineinput)
            print(scaleS)
            global fyield
            i=0
            while i<len(lineinput):
                if lineinput[i]=="code":
                    Code=lineinput[i+1]
                elif lineinput[i]=="fy":
                    fyield = float(lineinput[i+1])*scaleS
                i +=1    
            #print(fyield)
            lineinput.clear()
        child = child.GetNext()
