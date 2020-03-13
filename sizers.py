import wx

app=wx.PySimpleApp()
frame=wx.Frame(None,-1)

panel=wx.Panel(frame)
panel.SetBackgroundColour("black")
st1=wx.StaticText(panel,-1,label="Hello")
st1.SetBackgroundColour("red")
st2=wx.StaticText(panel,-1,"World")
st2.SetBackgroundColour("green")
bs=wx.BoxSizer(wx.HORIZONTAL)
bs.Add(st1,1)
bs.Add(st2,1)
panel.SetSizer(bs)
frame.Show(True)

app.MainLoop()