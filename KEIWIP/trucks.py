# use dialog box to get data, insert into database & display
# Still needs a search function to find information from different tables
# TextCtrl for user input for model and serial number and model. 
# This will tell sql what serial number is needed and the correct table to search.
# Trucks.sqlite needs tables based of make and model of the forklifts.

import wx
import sqlite3 as db

class MyDialog(wx.Dialog):

    def __init__(self):

        wx.Dialog.__init__(self, None, title="Model and Year")

        lbl = wx.StaticText(self, label='Enter Forklift Info', pos=(50, 10))

        self.serial_number = wx.TextCtrl(self, -1, '', pos=(50, 40))
        wx.StaticText(self, -1, 'Serial Number', pos=(175, 40))

        self.year = wx.TextCtrl(self, -1, '', (50, 80))
        wx.StaticText(self, -1, 'Year', (175, 80))

        self.model = wx.TextCtrl(self, -1, '', (50, 120))
        wx.StaticText(self, -1, 'Model', (175, 120))

        self.label = wx.StaticText(self, label="Choose Make", pos=(200, 10))
        make = ["toyota", "kamatsu", "hyster", "mitsubishi", "catepillar"]
        self.comboBox = wx.ComboBox(self, choices=make, pos=(275, 10) )

        okBtn = wx.Button(self, id=wx.ID_OK, pos=(135, 170))  # add wx.OK button


class DataList(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size=(480, 300))
        panel = wx.Panel(self, -1)
        
        self.list = wx.ListCtrl(panel, -1, style=wx.LC_REPORT, pos=(20, 50), size=(370, -1))
        # set up columns
        self.list.InsertColumn(0, 'Serial number', width=90)
        self.list.InsertColumn(1, 'Year', width=90)
        self.list.InsertColumn(2, 'Model', width=90)

        # setup combo box for the main screen
        self.label = wx.StaticText(panel, -1, label="Choose Make", pos=(150, 5))
        make = ["toyota", "kamatsu", "hyster", "mitsubishi", "catepillar"]
        self.comboBox = wx.ComboBox(panel, -1, choices=make, pos=(250, 5) )
        self.table_name = wx.StaticText(panel, -1, 'Forklift', pos=(50, 5))

        # set up buttons
        display = wx.Button(panel, -1, 'Display', size=(-1, 30), pos=(20, 215))
        insert = wx.Button(panel, -1, 'Insert Truck', size=(-1, 30), pos=(100, 215))
        cancel = wx.Button(panel, -1, 'Cancel', size=(-1, 30), pos=(200, 215))
        search = wx.Button(panel, -1, 'Search', size=(-1, 30), pos=(280, 215))

        display.Bind(wx.EVT_BUTTON, self.OnDisplay )  # bind buttons to event handlers
        insert.Bind(wx.EVT_BUTTON, self.OnAdd )
        cancel.Bind(wx.EVT_BUTTON, self.OnCancel)
        search.Bind(wx.EVT_BUTTON, self.search)
        self.Centre()

    def getAllData(self):
        # Get the selected make from the combo box
        selected_make = self.comboBox.GetValue()

        # Construct the SQL query based on the selected make
        query = f"SELECT * FROM {selected_make}"

        self.list.DeleteAllItems()  # Empty the list control
        con = db.connect('trucks.sqlite')  # Connect to the database
        cur = con.cursor()

        try:
            cur.execute(query)
            results = cur.fetchall()

            for row in results:
                self.list.Append(row)  # Add records to the list control

        except db.Error as error:
            dlg = wx.MessageDialog(self, str(error), 'Error occurred')
            dlg.ShowModal()  # Display error message

        finally:
            cur.close()
            con.close()

    def OnDisplay(self, event):

        try:
            self.getAllData()      # display whole table

        except db.Error as error:
            dlg = wx.MessageDialog(self, str(error), 'Error occured')
            dlg.ShowModal()       # display error message

    def OnAdd(self, event):
        dlg = MyDialog()      # create an instance of MyDialog
        btnID = dlg.ShowModal()
        if btnID == wx.ID_OK:
            sNum = dlg.serial_number.GetValue()  # get data from controls on dialog box
            yr = dlg.year.GetValue()
            mod = dlg.model.GetValue()


        if sNum != "" and yr != "" and mod != "":   # only if no blank values

            try:
                con = db.connect('trucks.sqlite')  # connect to db
                cur = con.cursor()
                #["toyota", "kamatsu", "hyster", "mitsubishi", "catepillar"]
                if dlg.comboBox.GetValue() == "toyota":
                    sql = "INSERT INTO toyota VALUES (?, ?, ?)"
                if dlg.comboBox.GetValue() == "kamatsu":
                    sql = "INSERT INTO kamatsu VALUES (?, ?, ?)"
                # if dlg.comboBox.GetValue() == "hyster":
                #     sql = "INSERT INTO hyster VALUES (?, ?, ?)"
                # if dlg.comboBox.GetValue() == "mitsubishi":
                #     sql = "INSERT INTO mitsubishi VALUES (?, ?, ?)"
                # if dlg.comboBox.GetValue() == "catepillar":
                #     sql = "INSERT INTO catepillar VALUES (?, ?, ?)"         

                cur.execute(sql, (sNum, yr, mod))
                con.commit()          # complete the transaction

                self.getAllData()     # display all data

            except db.Error as error:
                dlg = wx.MessageDialog(self, str(error), 'Error occured')
                dlg.ShowModal()        # display error message

        dlg.Destroy()

    def search(self, event):
        pass

    def OnCancel(self, event):
        self.Close()  # exit program

app = wx.App()
dl = DataList(None, -1, 'Insert Into Forklift')
dl.Show()
app.MainLoop()
