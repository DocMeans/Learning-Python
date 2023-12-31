import wx
from database import DatabaseManager

class ForkliftRepairApp(wx.Frame):
    def __init__(self, parent, title):
        super(ForkliftRepairApp, self).__init__(parent, title=title, size=(800,600))

        self.db_manager = DatabaseManager('main.db')
        self.InitUI()
        self.Centre()
        self.Show()
    

    def InitUI(self):
        panel = wx.Panel(self)
        
        #UI Elements
        self.list_ctrl = wx.ListCtrl(panel, size)