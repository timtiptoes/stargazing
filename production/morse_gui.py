#!/usr/bin/python

'''
To do
 - verify that this runs on  tegra
Improvements
-be able to pull up previous message and print
-log all messages sent
-pull down menu of stars
-spinning graphic of star with facts about star

'''


# -*- coding: iso-8859-1 -*-
# Taken from http://sebsauvage.net/python/gui/
#from sysfs.gpio import GPIOController
#from sysfs.gpio import GPIOPinDirection as Direction
#from sysfs.gpio import GPIOPinEdge as Edge

import csv
import time
import Tkinter
import subprocess




class simpleapp_tk(Tkinter.Tk):

    #star_data=[('alpha centauri','4.3'),('betelgeuse','95.6')]


    star_data={}
    star_names=[]
    f = open('../data/star_data.txt')
    csv_f = csv.reader(f)

    for row in csv_f:
	print row
  	star_names.append(row[0])
	star_data[row[0]]=[row[1:]]


#    star_names=[star[0] for star in csv_f]

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

	#Create pull down menu
        self.variable = Tkinter.StringVar()
        self.variable.set(self.star_names[0]) # default value
        self.w = apply(Tkinter.OptionMenu, (self, self.variable) + tuple(self.star_names))
        self.w.grid(column=1,row=0,sticky='EW')


	#Create text entry box
        self.entryVariable = Tkinter.StringVar()
        self.entry = Tkinter.Entry(self,textvariable=self.entryVariable)
        self.entry.grid(column=0,row=0,sticky='EW')
        self.entry.bind("<Return>", self.OnPressEnter)
        self.entryVariable.set(u"Enter text here.")
        self.labelVariable = Tkinter.StringVar()
        label = Tkinter.Label(self,textvariable=self.labelVariable,
                              anchor="w", fg="white", bg="black", font=("Courier", 300, "bold"))
	
	self.azelVariable = Tkinter.StringVar()
        azel = Tkinter.Label(self,textvariable=self.azelVariable,
                              anchor="w", fg="black", bg="white", font=("Courier", 12))
	azel.grid(column=0,row=1)

	button=Tkinter.Button(self,text=u"Send Message",command=self.OnPressOK)
	button.grid(column=1,row=1)
    
	label.grid(column=0,row=2,columnspan=2,sticky='EW')
        self.labelVariable.set(u"                ")

	


        self.grid_columnconfigure(0,weight=1)
        self.resizable(True,False)
        self.update()
        self.geometry(self.geometry())
        self.entry.focus_set()
        self.entry.selection_range(0, Tkinter.END)

    def OnPressEnter(self,event):
	star=self.variable.get()
	az=self.star_data[star][0][1]
	el=self.star_data[star][0][2]
	print "I got "+star+" and ("+str(az)+","+str(el)+")"
	self.azelVariable.set(" Go to "+str(az)+","+str(el))
        self.update_idletasks()




	#What to do when user presses OK
    def OnPressOK(self):
        input=self.entryVariable.get()
        for letter in input:
            if (letter == ' '):
                display_string = "<pause>"
            else:
                display_string = letter + ":   "
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
        self.labelVariable.set(display_string)
        self.update_idletasks()
        #self.print_out(display_string,self.variable.get())

    def dot(self):
  #      led_pin.set()

        time.sleep(0.2*self.factor)
#        led_pin.reset()
        time.sleep(0.2*self.factor)

    def dash(self):
#        led_pin.set()
#print "dash"
        time.sleep(0.5*self.factor)
#        led_pin.reset()
        time.sleep(0.2*self.factor)

    def print_out(self, message,star_name):
   	lpr =  subprocess.Popen("/usr/bin/lpr", stdin=subprocess.PIPE)
	output="*****************\n"
	
        output+= "Following message sent at " + time.ctime()+"\n"
        output+= message+"\n"
        output+= "star: "+star_name+"\n"
        output+= "*****************"
	lpr.stdin.write(output)
        lpr.stdin.close()


	print output
if __name__ == "__main__":
    app = simpleapp_tk(None)
    app.title('my application')
    app.mainloop()
