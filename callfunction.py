import random
import wx

########################################################################
class Panel(wx.Panel):
    """"""

    #----------------------------------------------------------------------
    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent)

        self.call_function = None
        self.choices = ["this", "that", "something", "other", "python"]

        btn = wx.Button(self, label="Change Variable Value")
        btn.Bind(wx.EVT_BUTTON, self.onButton)

    #----------------------------------------------------------------------
    def onButton(self, event):
        """
        Change the value of self.call_function
        """
        self.call_function = random.choice(self.choices)
        print (self.call_function)

########################################################################
class Frame(wx.Frame):
    """"""

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        wx.Frame.__init__(self, None, title="Return value")
        panel = Panel(self)
        self.Show()

#----------------------------------------------------------------------
if __name__ == "__main__":
    app = wx.App(False)
    frame = Frame()
    app.MainLoop()