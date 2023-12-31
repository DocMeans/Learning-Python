import wx
from database import DatabaseManager


class ForkliftRepairApp(wx.Frame):
    def __init__(self, parent, title):
        super(ForkliftRepairApp, self).__init__(parent, title=title, size=(800, 600))

        self.db_manager = DatabaseManager("main.db")
        self.InitUI()
        self.Centre()
        self.Show()

    def InitUI(self):
        panel = wx.Panel(self)

        # UI Elements
        self.list_ctrl = wx.ListCtrl(panel, size=(-1, 100))

        self.list_ctrl.InsertColumn(0, "ID", width=140)
        self.list_ctrl.InsertColumn(1, "Model", width=130)
        self.list_ctrl.InsertColumn(2, "Repair Status", width=130)

        # Layout with Sizers
        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(self.list_ctrl, 0, wx.EXPAND | wx.ALL, 20)
        panel.SetSizer(vbox)

        # Load Data
        self.load_data()

    def load_data(self):
        for row in self.db_manager.load_data():
            self.list_ctrl.Append(row)

    def OnClose(self, event):
        self.db_manager.close()
        self.Destroy()


if __name__ == "__main__":
    app = wx.App(False)
    frame = ForkliftRepairApp(None, "Forklift Repair Management")
    app.MainLoop()
