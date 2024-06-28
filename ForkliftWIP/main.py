# NEEDS an update function to fix incorrect entries.
# Trucks.sqlite needs tables based of make and model of the forklifts.
# NEEDS ability to add tables to the database
# make a functions.py script to handle database conn and search etc...


import wx
import sqlite3 as db
from dialogs import MyDialog, SearchDialog

from database import fetch_all_data  # Import other necessary functions


class DataList(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size=(480, 300))
        panel = wx.Panel(self, -1)

        self.list = wx.ListCtrl(
            panel, -1, style=wx.LC_REPORT, pos=(20, 50), size=(370, -1)
        )
        # set up columns
        self.list.InsertColumn(0, "Serial number", width=90)
        self.list.InsertColumn(1, "Year", width=90)
        self.list.InsertColumn(2, "Model", width=90)

        # setup combo box for the main screen
        self.label = wx.StaticText(panel, -1, label="Choose Make", pos=(150, 5))
        make = ["toyota", "kamatsu", "hyster", "mitsubishi", "catepillar"]
        self.comboBox = wx.ComboBox(panel, -1, choices=make, pos=(250, 5))
        self.table_name = wx.StaticText(panel, -1, "Forklift", pos=(50, 5))

        # set up buttons
        display = wx.Button(panel, -1, "Display", size=(-1, 30), pos=(20, 215))
        insert = wx.Button(panel, -1, "Insert Truck", size=(-1, 30), pos=(100, 215))
        cancel = wx.Button(panel, -1, "Cancel", size=(-1, 30), pos=(200, 215))
        search = wx.Button(panel, -1, "Search", size=(-1, 30), pos=(280, 215))

        display.Bind(wx.EVT_BUTTON, self.OnDisplay)  # bind buttons to event handlers
        insert.Bind(wx.EVT_BUTTON, self.OnAdd)
        cancel.Bind(wx.EVT_BUTTON, self.OnCancel)
        search.Bind(wx.EVT_BUTTON, self.OnSearch)
        self.Centre()

    def getAllData(self):
        # Get the selected make from the combo box
        selected_make = self.comboBox.GetValue()

        # Construct the SQL query based on the selected make
        query = f"SELECT * FROM {selected_make}"

        self.list.DeleteAllItems()  # Empty the list control
        con = db.connect("trucks.sqlite")  # Connect to the database
        cur = con.cursor()

        try:
            cur.execute(query)
            results = cur.fetchall()

            for row in results:
                self.list.Append(row)  # Add records to the list control

        except db.Error as error:
            dlg = wx.MessageDialog(self, str(error), "Error occurred")
            dlg.ShowModal()  # Display error message

        finally:
            cur.close()
            con.close()

    def OnDisplay(self, event):
        try:
            self.getAllData()  # display whole table

        except db.Error as error:
            dlg = wx.MessageDialog(self, str(error), "Error occured")
            dlg.ShowModal()  # display error message

    def OnAdd(self, event):
        dlg = MyDialog()  # create an instance of MyDialog
        btnID = dlg.ShowModal()
        if btnID == wx.ID_OK:
            sNum = dlg.serial_number.GetValue()  # get data from controls on dialog box
            yr = dlg.year.GetValue()
            mod = dlg.model.GetValue()

        if sNum != "" and yr != "" and mod != "":  # only if no blank values
            try:
                con = db.connect("trucks.sqlite")  # connect to db
                cur = con.cursor()
                # current tables ["toyota", "kamatsu", "hyster", "mitsubishi", "catepillar"]
                if dlg.comboBox.GetValue() == "toyota":
                    sql = "INSERT INTO toyota VALUES (?, ?, ?)"
                if dlg.comboBox.GetValue() == "kamatsu":
                    sql = "INSERT INTO kamatsu VALUES (?, ?, ?)"
                if dlg.comboBox.GetValue() == "hyster":
                    sql = "INSERT INTO hyster VALUES (?, ?, ?)"
                if dlg.comboBox.GetValue() == "mitsubishi":
                    sql = "INSERT INTO mitsubishi VALUES (?, ?, ?)"
                if dlg.comboBox.GetValue() == "catepillar":
                    sql = "INSERT INTO catepillar VALUES (?, ?, ?)"

                cur.execute(sql, (sNum, yr, mod))
                con.commit()  # complete the transaction

                self.getAllData()  # display all data

            except db.Error as error:
                dlg = wx.MessageDialog(self, str(error), "Error occurred")
                dlg.ShowModal()  # display error message

        dlg.Destroy()

    def OnSearch(self, event):
        make_choices = ["toyota", "kamatsu", "hyster", "mitsubishi", "catepillar"]
        dlg = SearchDialog("Search Forklift", make_choices)
        btnID = dlg.ShowModal()

        if btnID == wx.ID_OK:
            sNum = dlg.serial_number.GetValue()
            selected_make = dlg.comboBox.GetValue()

            if sNum != "":
                try:
                    con = db.connect("trucks.sqlite")
                    cur = con.cursor()

                    query = f"SELECT year FROM {selected_make} WHERE serial_number = ?"
                    cur.execute(query, (sNum,))
                    result = cur.fetchone()

                    if result:
                        wx.MessageBox(
                            f"The forklift with serial number {sNum} from {selected_make} was made in {result[0]}",
                            "Search Result",
                            wx.OK | wx.ICON_INFORMATION,
                        )
                    else:
                        wx.MessageBox(
                            f"No record found for serial number {sNum} in {selected_make}",
                            "Search Result",
                            wx.OK | wx.ICON_INFORMATION,
                        )

                except db.Error as error:
                    dlg = wx.MessageDialog(self, str(error), "Error occurred")
                    dlg.ShowModal()

        dlg.Destroy()

    def OnCancel(self, event):
        self.Close()  # exit program


app = wx.App()
dl = DataList(None, -1, "Forklift Information")
dl.Show()
app.MainLoop()

'''
import wx
import sqlite3 as db
from dialogs import MyDialog, SearchDialog

from database import fetch_all_data  # Import other necessary functions


class DataList(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size=(480, 600))
        panel = wx.Panel(self, -1)

        self.list = wx.ListCtrl(
            panel, -1, style=wx.LC_REPORT, pos=(20, 50), size=(370, -1)
        )
        # set up columns
        self.list.InsertColumn(0, "Serial number", width=90)
        self.list.InsertColumn(1, "Year", width=90)
        self.list.InsertColumn(2, "Model", width=90)

        # setup text input for the brand on the main screen
        self.label = wx.StaticText(panel, -1, label="Enter Brand", pos=(150, 5))
        self.brand_txt = wx.TextCtrl(panel, -1, pos=(250, 5))
        self.table_name = wx.StaticText(panel, -1, "Forklift", pos=(50, 5))

        # set up buttons
        display = wx.Button(panel, -1, "Display", size=(-1, 30), pos=(20, 215))
        insert = wx.Button(panel, -1, "Insert Truck", size=(-1, 30), pos=(100, 215))
        cancel = wx.Button(panel, -1, "Cancel", size=(-1, 30), pos=(200, 215))
        search = wx.Button(panel, -1, "Search", size=(-1, 30), pos=(280, 215))

        display.Bind(wx.EVT_BUTTON, self.OnDisplay)  # bind buttons to event handlers
        insert.Bind(wx.EVT_BUTTON, self.OnAdd)
        cancel.Bind(wx.EVT_BUTTON, self.OnCancel)
        search.Bind(wx.EVT_BUTTON, self.OnSearch)
        self.Centre()

    def getAllData(self):
        # Get the entered brand from the text input
        entered_brand = self.brand_txt.GetValue().lower()

        # Construct the SQL query based on the entered brand
        query = f"SELECT * FROM {entered_brand}"

        self.list.DeleteAllItems()  # Empty the list control
        con = db.connect("trucks.sqlite")  # Connect to the database
        cur = con.cursor()

        try:
            cur.execute(query)
            results = cur.fetchall()

            for row in results:
                self.list.Append(row)  # Add records to the list control

        except db.Error as error:
            dlg = wx.MessageDialog(self, str(error), "Error occurred")
            dlg.ShowModal()  # Display error message

        finally:
            cur.close()
            con.close()

    def OnDisplay(self, event):
        try:
            self.getAllData()  # display whole table

        except db.Error as error:
            dlg = wx.MessageDialog(self, str(error), "Error occurred")
            dlg.ShowModal()  # display error message

    def OnAdd(self, event):
        dlg = MyDialog()  # create an instance of MyDialog
        btnID = dlg.ShowModal()
        if btnID == wx.ID_OK:
            sNum = dlg.serial_number.GetValue()  # get data from controls on dialog box
            yr = dlg.year.GetValue()
            mod = dlg.model.GetValue()
            brand = dlg.brand.GetValue().lower()
            oil_filter = dlg.oil_filter.GetValue()
            alt_oil_filter = dlg.alt_oil_filter.GetValue()

        if sNum != "" and yr != "" and mod != "" and brand != "":  # only if no blank values
            try:
                con = db.connect("trucks.sqlite")  # connect to db
                cur = con.cursor()
                sql = f"INSERT INTO {brand} (serial_number, year, model, oil_filter, alt_oil_filter) VALUES (?, ?, ?, ?, ?)"

                cur.execute(sql, (sNum, yr, mod, oil_filter, alt_oil_filter))
                con.commit()  # complete the transaction

                self.getAllData()  # display all data

            except db.Error as error:
                dlg = wx.MessageDialog(self, str(error), "Error occurred")
                dlg.ShowModal()  # display error message

        dlg.Destroy()

    def OnSearch(self, event):
        dlg = SearchDialog("Search Forklift")
        btnID = dlg.ShowModal()

        if btnID == wx.ID_OK:
            sNum = dlg.serial_number.GetValue()
            entered_brand = dlg.brand.GetValue().lower()

            if sNum != "" and entered_brand != "":
                try:
                    con = db.connect("trucks.sqlite")
                    cur = con.cursor()

                    query = f"SELECT year FROM {entered_brand} WHERE serial_number = ?"
                    cur.execute(query, (sNum,))
                    result = cur.fetchone()

                    if result:
                        wx.MessageBox(
                            f"The forklift with serial number {sNum} from {entered_brand} was made in {result[0]}",
                            "Search Result",
                            wx.OK | wx.ICON_INFORMATION,
                        )
                    else:
                        wx.MessageBox(
                            f"No record found for serial number {sNum} in {entered_brand}",
                            "Search Result",
                            wx.OK | wx.ICON_INFORMATION,
                        )

                except db.Error as error:
                    dlg = wx.MessageDialog(self, str(error), "Error occurred")
                    dlg.ShowModal()

        dlg.Destroy()

    def OnCancel(self, event):
        self.Close()  # exit program


app = wx.App()
dl = DataList(None, -1, "Forklift Information")
dl.Show()
app.MainLoop()
'''