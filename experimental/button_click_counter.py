__author__ = 'timtiptoes'

from Tkinter import *

class Application(Frame):
    """A GUI application with three buttons. """

    def __init__(self, master):
        """
        :param master: Initialize the frame"""
        Frame.__init__(self, master)
        self.grid()
        self.button_clicks = 1  #count the number of button clicks
        self.create_widgets()

    def create_widgets(self):
        """Create button the number of clicks"""
        #create first button
        self.button1 = Button(self)
        self.button1["text"]="Total Clicks: 0"
        self.button1["command"] = self.update_count
        self.button1.grid()

    def update_count(self):
        """Increase the click count and display the new total"""
        self.button_clicks +=1
        self.button1["text"] = "Total Clicks: " +str(self.button_clicks)



root = Tk()
root.title("Lazy Buttons")
root.geometry("200x85")

app = Application(root)
root.mainloop()
