import wx
#classes

class MyDialog(wx.Dialog):
    def __init__(self):
        wx.Dialog.__init__(self, None, title="Model and Year")

        lbl = wx.StaticText(self, label="Enter Forklift Info", pos=(50, 10))

        self.serial_number = wx.TextCtrl(self, -1, "", pos=(50, 40))
        wx.StaticText(self, -1, "Serial Number", pos=(175, 40))

        self.year = wx.TextCtrl(self, -1, "", (50, 80))
        wx.StaticText(self, -1, "Year", (175, 80))

        self.model = wx.TextCtrl(self, -1, "", (50, 120))
        wx.StaticText(self, -1, "Model", (175, 120))

        self.label = wx.StaticText(self, label="Choose Make", pos=(200, 10))
        make = ["toyota", "kamatsu", "hyster", "mitsubishi", "catepillar"]
        self.comboBox = wx.ComboBox(self, choices=make, pos=(275, 10))

        okBtn = wx.Button(self, id=wx.ID_OK, pos=(135, 170))  # add wx.OK button


class SearchDialog(wx.Dialog):
    def __init__(self, title, make_choices):
        wx.Dialog.__init__(self, None, title=title)

        lbl = wx.StaticText(self, label="Search Forklift", pos=(50, 10))

        self.serial_number = wx.TextCtrl(self, -1, "", pos=(50, 40))
        wx.StaticText(self, -1, "Serial Number", pos=(175, 40))

        self.make_choices = make_choices
        self.comboBox = wx.ComboBox(
            self, -1, choices=make_choices, pos=(50, 80), style=wx.CB_READONLY
        )
        wx.StaticText(self, -1, "Choose Make", pos=(175, 80))

        okBtn = wx.Button(self, id=wx.ID_OK, pos=(135, 120))  # add wx.OK button

'''
import wx

# classes

class MyDialog(wx.Dialog):
    def __init__(self):
        wx.Dialog.__init__(self, None, title="Model and Year", size=(400, 450))

        lbl = wx.StaticText(self, label="Enter Forklift Info", pos=(50, 10))

        self.serial_number = wx.TextCtrl(self, -1, "", pos=(50, 40))
        wx.StaticText(self, -1, "Serial Number", pos=(175, 40))

        self.year = wx.TextCtrl(self, -1, "", (50, 80))
        wx.StaticText(self, -1, "Year", (175, 80))

        self.model = wx.TextCtrl(self, -1, "", (50, 120))
        wx.StaticText(self, -1, "Model", (175, 120))

        self.brand = wx.TextCtrl(self, -1, "", (50, 160))
        wx.StaticText(self, -1, "Brand", (175, 160))
        
        self.oil_filter = wx.TextCtrl(self, -1, "", (50, 200))
        wx.StaticText(self, -1, "Oil Filter", (175, 200))

        self.alt_oil_filter = wx.TextCtrl(self, -1, "", (50, 240))
        wx.StaticText(self, -1, "Alt Oil Filter", (175, 240))

        okBtn = wx.Button(self, id=wx.ID_OK, pos=(135, 280))  # add wx.OK button

class SearchDialog(wx.Dialog):
    def __init__(self, title):
        wx.Dialog.__init__(self, None, title=title)

        lbl = wx.StaticText(self, label="Search Forklift", pos=(50, 10))

        self.serial_number = wx.TextCtrl(self, -1, "", pos=(50, 40))
        wx.StaticText(self, -1, "Serial Number", pos=(175, 40))

        self.brand = wx.TextCtrl(self, -1, "", (50, 80))
        wx.StaticText(self, -1, "Brand", (175, 80))

        self.oil_filter = wx.TextCtrl(self, -1, "", (50, 120))
        wx.StaticText(self, -1, "Oil Filter", (175, 120))

        self.alt_oil_filter = wx.TextCtrl(self, -1, "", (50, 160))
        wx.StaticText(self, -1, "Alt Oil Filter", (175, 160))

        okBtn = wx.Button(self, id=wx.ID_OK, pos=(135, 200))  # add wx.OK button

# Initialize the application
app = wx.App(False)

# For demonstration purposes, show MyDialog first
dlg = MyDialog()
dlg.ShowModal()
dlg.Destroy()

# Show SearchDialog
search_dlg = SearchDialog("Search Forklift")
search_dlg.ShowModal()
search_dlg.Destroy()

app.MainLoop()
'''