#!/usr/bin/python
# -*- coding: iso-8859-1 -*-
# Taken from http://sebsauvage.net/python/gui/
# from sysfs.gpio import GPIOController
# from sysfs.gpio import GPIOPinDirection as Direction
# from sysfs.gpio import GPIOPinEdge as Edge
import time
import Tkinter

class simpleapp_tk(Tkinter.Tk):

    CODE = {' ': ' ',
        "'": '.----.',
        '(': '-.--.-',
        ')': '-.--.-',
        ',': '--..--',
        '-': '-....-',
        '.': '.-.-.-',
        '/': '-..-.',
        '0': '-----',
        '1': '.----',
        '2': '..---',
        '3': '...--',
        '4': '....-',
        '5': '.....',
        '6': '-....',
        '7': '--...',
        '8': '---..',
        '9': '----.',
        ':': '---...',
        ';': '-.-.-.',
        '?': '..--..',
        'A': '.-',
        'B': '-...',
        'C': '-.-.',
        'D': '-..',
        'E': '.',
        'F': '..-.',
        'G': '--.',
        'H': '....',
        'I': '..',
        'J': '.---',
        'K': '-.-',
        'L': '.-..',
        'M': '--',
        'N': '-.',
        'O': '---',
        'P': '.--.',
        'Q': '--.-',
        'R': '.-.',
        'S': '...',
        'T': '-',
        'U': '..-',
        'V': '...-',
        'W': '.--',
        'X': '-..-',
        'Y': '-.--',
        'Z': '--..',
        '_': '..--.-'}

    #GPIOController().available_pins = [57]

#led_pin=GPIOController().alloc_pin(57,Direction.OUTPUT)
    factor=1

    def __init__(self,parent):
        Tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.grid()

        self.entryVariable = Tkinter.StringVar()
        self.entry = Tkinter.Entry(self,textvariable=self.entryVariable)
        self.entry.grid(column=0,row=0,sticky='EW')
        self.entry.bind("<Return>", self.OnPressEnter)
        self.entryVariable.set(u"Enter text here.")

        button = Tkinter.Button(self,text=u"Click me !",
                                command=self.OnButtonClick)
        button.grid(column=1,row=0)

        self.labelVariable = Tkinter.StringVar()
        label = Tkinter.Label(self,textvariable=self.labelVariable,
                              anchor="w",fg="white",bg="black",font=("Courier", 300,"bold"))
        label.grid(column=0,row=1,columnspan=2,sticky='EW')
        self.labelVariable.set(u"Hello !")

####
        self.label2Variable = Tkinter.StringVar()
        label2 = Tkinter.Label(self,textvariable=self.label2Variable,
                              anchor="w",fg="white",bg="black",font=("Courier", 100,"bold"))
        label2.grid(column=0,row=2,columnspan=2,sticky='EW')
        self.label2Variable.set(u"")
####

        self.grid_columnconfigure(0,weight=1)
        self.resizable(True,False)
        self.update()
        self.geometry(self.geometry())
        self.entry.focus_set()
        self.entry.selection_range(0, Tkinter.END)

    def OnButtonClick(self):
        self.labelVariable.set( self.entryVariable.get()+" (You clicked the button)" )
        self.entry.focus_set()
        self.entry.selection_range(0, Tkinter.END)

    def OnPressEnter(self,event):
        input=self.entryVariable.get()
        for letter in input:
            display_string=letter+":   "
            self.labelVariable.set(display_string)
            self.update_idletasks()
            for symbol in self.CODE[letter.upper()]:
                if symbol == '-':
                    display_string+="-"
                    self.labelVariable.set(display_string)
                    self.update_idletasks()
                    self.dash()
                elif symbol == '.':
                    display_string+=unichr(0x2022)
                    self.labelVariable.set(display_string)
                    self.update_idletasks()
                    self.dot()
                else:
                    time.sleep(0.5*self.factor)
            time.sleep(0.5*self.factor)

        self.entry.focus_set()
        self.entry.selection_range(0, Tkinter.END)
        display_string=input
        self.labelVariable.set(u"")

        self.label2Variable.set("sent: "+display_string)
        self.update_idletasks()

    def dot(self):
#        led_pin.set()
        print "dot"
        time.sleep(0.2*self.factor)
#        led_pin.reset()
        time.sleep(0.2*self.factor)

    def dash(self):
#        led_pin.set()
        print "dash"
        time.sleep(0.5*self.factor)
#        led_pin.reset()
        time.sleep(0.2*self.factor)

if __name__ == "__main__":
    app = simpleapp_tk(None)
    app.title('my application')
    app.mainloop()
