import wx 
import os 
import xml.etree.ElementTree as ET

class MyFrame(wx.Frame): 
   
   def __init__(self, parent, title): 
      super(MyFrame, self).__init__(parent, title = title,size=(600,500)) 
      
      #Set the panel
      self.panel=MyPanel(self)
      

      
class App(wx.App):
       
   def OnInit(self):
      self.frame=MyFrame(parent=None, title='Wire3D')
      self.frame.Show()
      return True  

      

        
class MyPanel(wx.Panel) :
       
   def __init__(self,parent):
      super(MyPanel,self).__init__(parent)
      
      sizer=wx.BoxSizer(wx.HORIZONTAL)
      self.button1 = wx.Button(self, label="Button 1")
      sizer.Add(self.button1,0)
      self.button1.Bind(wx.EVT_BUTTON,self.OnButton,self.button1)
                  
      self.button2 = wx.Button(self, label="Button 2")
      sizer.Add(self.button2)
      self.button2.Bind(wx.EVT_BUTTON,self.OnFrameExit,self.button2)       


      self.SetSizer(sizer)
            
      
   def OnButton(self, event):
      button = event.EventObject
      print("Button (%s) event at Panel!" % button.Label)
      if button is self.button1:
         event.Skip()
         
   def OnFrameExit(self,event) :
      theFrame=event.EventObject
      print("Frame(%s)is closing!"%theFrame.Title) 
      event.Skip()           
      


if __name__ == '__main__':

   ex =App()

   ex.MainLoop()