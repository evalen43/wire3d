import wx 
import os 
import xml.etree.ElementTree as ET

class MyFrame(wx.Frame): 
   
   def __init__(self, parent, title): 
      super(MyFrame, self).__init__(parent, title = title,size=(1000,500)) 
      
      #Set the panel
      self.panel=MyPanel(self)
      
      self.menuSetup()
      
   def menuSetup(self):
      menuBar=wx.MenuBar()
      m_FileMenu=wx.Menu()
      m_HelpMenu=wx.Menu()
      exitItem=m_FileMenu.Append(wx.ID_EXIT,'&Quit','status mag...')
      openItem=m_FileMenu.Append(wx.ID_OPEN,'&Open')
      menuBar.Append(m_FileMenu,'&File')
      menuBar.Append(m_HelpMenu,'&Help')      
      m_FileMenu.Append(wx.ID_OPEN,'&Open')
      m_FileMenu.Append(wx.ID_SAVE,'&Save')  
      m_FileMenu.Append(wx.ID_EXIT,'&Quit')
      m_HelpMenu.Append(wx.ID_ABOUT,'&About')                    
      self.SetMenuBar(menuBar)
      self.Bind(wx.EVT_MENU,self.Quit,exitItem)
      self.Bind(wx.EVT_MENU,self.Open,openItem)      
      #self.SetTitle('Epic Window')  
      #self.Show(True)  
   def Quit(self,e) :
      self.Close()   
   def Open(self, e): 
      wildcard = "XML Files (*.xml)|*.xml"
      dlg = wx.FileDialog(self, "Choose a file", os.getcwd(), "", wildcard, wx.FD_OPEN)
      if dlg.ShowModal() == wx.ID_OK: 
         f = open(dlg.GetPath(), 'r') 
         with f: 
            data = f.read() 
            self.panel.textout.SetValue(data)
         fname=f.name 
      dlg.Destroy()
      return fname        
class App(wx.App):
       
   def OnInit(self):
      self.frame=MyFrame(parent=None, title='Wire3D')
      self.frame.Show()
      return True  
        
class MyPanel(wx.Panel) :
       
   def __init__(self,parent):
      super(MyPanel,self).__init__(parent)
      

      
      vbox = wx.BoxSizer(wx.VERTICAL) 
      #vbox1 = wx.BoxSizer(wx.VERTICAL) 
      hbox1 = wx.BoxSizer(wx.HORIZONTAL) 
      hbox2 = wx.BoxSizer(wx.HORIZONTAL) 
      hbox3 = wx.BoxSizer(wx.HORIZONTAL) 
      hbox4 = wx.BoxSizer(wx.HORIZONTAL) 
      #hbox5 = wx.BoxSizer(wx.HORIZONTAL)
       
      self.text = wx.TextCtrl(self, -1,"Click Button Open File......",wx.DefaultPosition,size = (400,300),style = wx.TE_MULTILINE)
      self.textout = wx.TextCtrl(self, -1,"Click Button to see Results......",wx.DefaultPosition,size = (400,300),style = wx.TE_MULTILINE)
      self.btn1 = wx.Button(self, label = "Open a File")
      self.btn2=wx.Button(self, label="Exit") 
      self.btn1.Bind(wx.EVT_BUTTON, self.OnClick) 
      self.btn2.Bind(wx.EVT_BUTTON,self.OnExit)
      self.lbl1=wx.StaticText(self,label="Below is the Content of the Input File")
      
      hbox1.Add(self.btn1, proportion = 1, flag = wx.LEFT, border = 10)  
      hbox2.Add(self.lbl1, proportion = 1, flag = wx.LEFT, border = 10)            
      hbox3.Add(self.text, proportion = 1)#, flag = wx.EXPAND|wx.ALIGN_CENTRE,border=15)
      hbox3.Add(self.textout, proportion = 1)#, flag = wx.EXPAND|wx.ALIGN_CENTRE,border=15)
      hbox4.Add(self.btn2, proportion = 1, flag = wx.LEFT, border = 10) 

      #hbox5.Add(self.textout, proportion = 1, flag = wx.EXPAND|wx.ALIGN_CENTRE,border=15)
      
      vbox.Add(hbox1, proportion = 1, flag = wx.ALIGN_LEFT,border=10) 
      vbox.Add(hbox2, proportion = 1, flag = wx.ALIGN_LEFT,border=10)    
      vbox.Add(hbox3, proportion = 1, flag = wx.EXPAND|wx.ALIGN_LEFT,border=10)
      vbox.Add(hbox4, proportion = 1, flag = wx.ALIGN_LEFT,border=10)
      #vbox1.Add(hbox5, proportion = 1, flag = wx.ALIGN_LEFT,border=10)

      self.SetSizerAndFit(vbox)
      #self.SetSizer(vbox1) 
            
      
   def OnClick(self, event):
      button = event.EventObject
      print("Button (%s) event at Panel!" % button.Label)
      if button is self.button1:
         #event.Skip()
         self.Open()
         
   def OnExit(self,event) :
      button = event.EventObject
      if button is self.button1:          
         self.Close()
         event.Skip()           
      '''theFrame=event.EventObject
      print("Frame(%s)is closing!"%theFrame.Title) '''
      
                
     


if __name__ == '__main__':

   ex =App()

   ex.MainLoop()