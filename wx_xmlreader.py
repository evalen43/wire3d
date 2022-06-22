import wx
from tokenize import tokenize, untokenize, NUMBER, STRING, NAME, OP
from io import BytesIO
def XML_reader(filein):

    doc = wx.xml.XmlDocument()
    if not doc.Load(filein):
        return False
    # start processing the XML file
    # if doc.GetRoot().GetName() != "myroot-node":
    #     return False
    strutype = doc.GetRoot().GetName()

    # examine childue
    #child = doc.GetDocumentNode().GetChildren()
    # while child:

    #     if child.GetType() == wx.xml.XML_PI_NODE and child.GetName() == "target":

    #         # process Process Instruction contents
    #         pi = child.GetContent()

            # Other code here...
    child = doc.GetRoot().GetChildren()
    while child:
        tagname = child.GetName()
        content = child.GetNodeContent()  # process text enclosed by tag1/tag1
        scaleS = 0.0
        lineinput=[""]
        if tagname == "title":
            projName=content
            # # process attributes of tag1
            # attrvalue1 = child.GetAttribute("attr1", "default-value")
            #attrvalue2 = child.GetAttribute("attr2", "default-value")
        elif tagname == "code":
            UnitS = child.GetAttribute("unitS", "kN/m2")  # UnitS: stress unit ...
            if UnitS == "default-value":
                scaleS=1.0                
            tokens=tokenize.generate_tokens(content)
            for token in tokens:
                lineinput.append(token)
            for x in lineinput:
                if x=="AISC":
                    Code=x
                elif x=="fy":
                    fyield=float(x)*scaleS        
        child = child.GetNext()
