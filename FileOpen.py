import wx 
import os 
import xml.etree.ElementTree as ET

class Mywin(wx.Frame): 

   
   def __init__(self, parent, title): 
      super(Mywin, self).__init__(parent, title = title)  
         
      self.InitUI() 
         
   def InitUI(self):    
      self.count = 0 
      pnl = wx.Panel(self) 
      vbox = wx.BoxSizer(wx.VERTICAL) 
      hbox1 = wx.BoxSizer(wx.HORIZONTAL) 
      hbox2 = wx.BoxSizer(wx.HORIZONTAL) 
      hbox3 = wx.BoxSizer(wx.HORIZONTAL) 
      hbox4 = wx.BoxSizer(wx.HORIZONTAL) 
		
      self.text = wx.TextCtrl(pnl, size = (-1,200),style = wx.TE_MULTILINE) 
      self.btn1 = wx.Button(pnl, label = "Open a File")
      self.btn2=wx.Button(pnl, label="Exit") 
      self.Bind(wx.EVT_BUTTON, self.OnClick, self.btn1) 
      self.Bind(wx.EVT_BUTTON,self.OnExit,self.btn2)
      self.lbl1=wx.StaticText(pnl,label="Input File")
		
      hbox1.Add(self.text, proportion = 1, flag = wx.ALIGN_CENTRE) 
      hbox2.Add(self.btn1, proportion = 1, flag = wx.RIGHT, border = 10) 
      hbox4.Add(self.btn2, proportion = 1, flag = wx.LEFT, border = 10) 
      hbox3.Add(self.lbl1, proportion = 1, flag = wx.LEFT, border = 10) 
      
      vbox.Add(hbox2, proportion = 1, flag = wx.ALIGN_CENTRE,border=10) 
      vbox.Add(hbox3, proportion = 1, flag = wx.ALIGN_LEFT,border=10)    
      vbox.Add(hbox1, proportion = 1, flag = wx.EXPAND|wx.ALIGN_LEFT,border=10) 
      vbox.Add(hbox4, proportion = 1, flag = wx.EXPAND|wx.ALIGN_LEFT,border=10)
         
      pnl.SetSizer(vbox) 
      self.Centre() 
      self.Show(True) 
        
   def OnExit(self, e):
      exit()
      
   def OnClick(self, e): 
      wildcard = "XML Files (*.xml)|*.xml"
      dlg = wx.FileDialog(self, "Choose a file", os.getcwd(), "", wildcard, wx.FD_OPEN)
      if dlg.ShowModal() == wx.ID_OK: 
         f = open(dlg.GetPath(), 'r') 
         with f: 
            data = f.read() 
            self.text.SetValue(data)
         fname=f.name 
      dlg.Destroy()
      return fname 

                                  
ex = wx.App() 
myw=Mywin(None, 'XML FileDialog Demo')
'''fname=myw.fname
mytree=ET.parse(fname)
myroot=mytree.getroot()      
      
#ScanDocument(f.name) 

for param in myroot :
   print(param.tag,param.attrib) 
   for child in myroot :
      print(child.tag,child.attrib) ''' 
ex.MainLoop()