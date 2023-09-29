'''
Written by: Franklin Means
09/28/2023
'''

import wx
class ShippingFrame(wx.Frame):
    def __init__(self, parent, id=wx.ID_ANY, title='Shipping Calculator'):
        super(ShippingFrame, self).__init__(parent, id, title, size = (425, 460)) # instantiate super class
        # Add a panel and add a label to the panel by calling their constructors
        self.panel = wx.Panel(self)
        #Text boxes and labels
        self.txt_name = wx.TextCtrl(self.panel, pos=(30, 30))
        self.lbl_name = wx.StaticText(self.panel, id=-1, pos=(150,30), label='Name')

        self.txt_address = wx.TextCtrl(self.panel, pos=(30, 60), size=(200,25))
        self.lbl_address = wx.StaticText(self.panel, id=-1, pos=(250,60), label='Adress')

        self.txt_city = wx.TextCtrl(self.panel, pos=(30, 90), size=(150, 25))
        self.lbl_city = wx.StaticText(self.panel, id=-1, pos=(200,90), label='City, State, and Zip')
        #Radio buttons and labels
        self.lbl_weight = wx.StaticText(self.panel, id=-1, pos=(55,140), label='Weight')
        self.weight1 = wx.RadioButton(self.panel, -1, label='0-1.9 lbs. $5.00', pos=(30, 160), style = wx.RB_GROUP) 
        self.weight2 = wx.RadioButton(self.panel, -1, label='2-4.9 lbs $8.00', pos=(30, 180)) 
        self.weight3 = wx.RadioButton(self.panel, -1, label='5-10 lbs $12.25', pos=(30, 200))
        
        self.lbl_speed = wx.StaticText(self.panel, id=-1, pos=(175,140), label='Speed')
        self.speed1 = wx.RadioButton(self.panel, -1, label='Overland $2.75', pos=(150, 160), style = wx.RB_GROUP) 
        self.speed2 = wx.RadioButton(self.panel, -1, label='3-day Air $6.15', pos=(150, 180)) 
        self.speed3 = wx.RadioButton(self.panel, -1, label='2-day Air $10.70', pos=(150, 200))
        self.speed4 = wx.RadioButton(self.panel, -1, label='Overnight $15.50', pos=(150, 220))
        # Checkboxes and labels
        self.lbl_options = wx.StaticText(self.panel, id=-1, pos=(305,140), label='Options')
        self.option1 = wx.CheckBox(self.panel, -1, label='Extra Padding $4', pos=(280, 160), style = wx.RB_GROUP)
        self.option2 = wx.CheckBox(self.panel, -1, label='Gift Wrapping $6', pos=(280, 180))
        # Buttons with names
        self.btn_total = wx.Button(self.panel, label="Calculate Total", pos=(50, 255))
        self.btn_clear = wx.Button(self.panel, label="Clear Form", pos=(250, 255))
        # these are blank at the bottom of the app until the calculate_price function is called
        self.lbl_summary = wx.StaticText(self.panel, id=-1, pos=(125,290), label='Shipping Summary')
        self.lbl_name_summary = wx.StaticText(self.panel, id=-1, pos=(100,320), label='')
        self.lbl_address_summary = wx.StaticText(self.panel, id=-1, pos=(100,340), label='')
        self.lbl_city_summary = wx.StaticText(self.panel, id=-1, pos=(100,360), label='')
        self.lbl_price = wx.StaticText(self.panel, id=-1, pos=(100,380), label='$ 0')
        # Binds the buttons to a function
        self.btn_clear.Bind(wx.EVT_BUTTON, self.clear)
        self.btn_total.Bind(wx.EVT_BUTTON, self.calculate_price)
    # This function reset the form back to default
    def clear(self, event):
        self.txt_name.SetValue("")
        self.lbl_name_summary.SetLabel("")
        self.txt_address.SetValue("")
        self.lbl_address_summary.SetLabel("")
        self.txt_city.SetValue("")
        self.lbl_city_summary.SetLabel("")
        self.lbl_price.SetLabel("$ 0")
        self.speed1.SetValue(1)
        self.weight1.SetValue(1)
        self.option1.SetValue(0)
        self.option2.SetValue(0)
    # This Calculates the total price and sends the price and shipping information to the summary
    def calculate_price(self, event):
        price = 0
        weight = 0
        speed = 0
        option = 0
        # first group of radio buttons with values
        if self.weight1.GetValue():
            weight = 5.00
        elif self.weight2.GetValue():
            weight = 8.00
        else:
            weight = 12.25
        # second group of radio buttons with values
        if self.speed1.GetValue():
            speed = 2.75
        elif self.speed2.GetValue():
            speed = 6.15
        elif self.speed3.GetValue():
            speed = 10.70            
        else:
            speed = 15.00
        # Checkboxes with values
        if self.option1.GetValue():
            option += 4.00
        if self.option2.GetValue():
            option += 6.00
        # Calculation is preformed here by adding all the variables together
        price = weight + speed + option
        # Total is formatted and then sent to the appropiate label
        cost = f"$ {price}"
        self.lbl_price.SetLabel(cost)
        # The information the user inputs is sent to the labels at the bottom of the form
        name = self.txt_name.GetValue()
        self.lbl_name_summary.SetLabel(name)
        address = self.txt_address.GetValue()
        self.lbl_address_summary.SetLabel(address)
        city = self.txt_city.GetValue()
        self.lbl_city_summary.SetLabel(city)

if __name__ == "__main__":
    app = wx.App() # create wxPython
    fr = ShippingFrame(None) # instantiate parent frame
    fr.Show() # display frame
    app.MainLoop() # start event loop