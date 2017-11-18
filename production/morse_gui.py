#!/usr/bin/python

if not(__debug__): from sysfs.gpio import GPIOController
if not(__debug__): from sysfs.gpio import GPIOPinDirection as Direction
if not(__debug__): from sysfs.gpio import GPIOPinEdge as Edge

#2016-11-19
#Some things to remind you:
#To run this, run sudo python -O morse_gui.py  the -O makes the __debug__ flag false, so it will click and print
#You need to modify the printer's form feed length from the default of 11" to 5.5" for both page length and page cut length
#To access settings. Press 'MODE' button and 'menu' should illuminiate. Then press "GROUP' until 'Vertical Control' Then Item until you
#see one of page length and page cut length and then item until you get to 5.5 and 5.5
#After typing in the message you have to hit return and THEN click 'Send Message'
import csv
import time
import datetime
import Tkinter
import subprocess
import math


class simpleapp_tk(Tkinter.Tk):

    star_data={}
    star_names=[]
    f = open('../data/star_data.txt')
    csv_f = csv.reader(f)
    next(f)
    for row in csv_f:
        print row
        star_names.append(row[0])
        star_data[row[0]]=row[1:]

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



    if not(__debug__): GPIOController().available_pins = [57]

    if not(__debug__): led_pin=GPIOController().alloc_pin(57,Direction.OUTPUT)
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
                              anchor="w", fg="white", bg="black", font=("Courier", 200, "bold"))

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
        self.star=self.variable.get()
        print self.star
        print self.star_data[self.star]
        (self.distance,self.az,self.el,self.star_type,self.spectral_type,self.funfact)=self.star_data[self.star]

        print self.star_data[self.star]
        #az=self.star_data[star][0][1]
        #el=self.star_data[star][0][2]
        print "I got "+self.star+" and ("+str(self.az)+","+str(self.el)+")"
        self.azelVariable.set(" Go to "+str(self.az)+","+str(self.el))
        self.update_idletasks()

    def power(self,d): return (1.79e-22)/(d*d)


    #What to do when user presses OK
    def OnPressOK(self):
        inputfull=self.entryVariable.get()
        input=inputfull[:140]
	if len(input)>10:
	        self.factor=0.1/(1+(len(input)-10)/130)
	else:
		self.factor=0.1
        coded_output=""
        for letter in input:
            if (letter == ' '):
                display_string = "<space>"
                time.sleep(7*self.factor)
                coded_output+=" "
            else:
                coded_output+=self.CODE[letter.upper()]+" "
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
            time.sleep(3*self.factor)


        self.entry.focus_set()
        self.entry.selection_range(0, Tkinter.END)
        display_string=input
        self.labelVariable.set(display_string)
        self.update_idletasks()
        self.print_out(display_string,coded_output)

    def dot(self):
        if not(__debug__): self.led_pin.set()
        time.sleep(self.factor)
        if not(__debug__): self.led_pin.reset()
        time.sleep(self.factor)

    def dash(self):
        if not(__debug__): self.led_pin.set()
#print "dash"
        time.sleep(3*self.factor)
        if not(__debug__): self.led_pin.reset()
        time.sleep(self.factor)

    def print_out(self, message,coded_output):
        '''
What I want it to say
    Message: hi honey
    Date Sent: 2015-11-16 18:55:43
    Target: Polaris
    Type: Brown Dwarf
    Size: 4 sols
    Distance: 123 light years (6,870,000,000,000 miles)
    Date of return: 2223-11-16 (262 years from now)
    Transmitted wavelength: 421nm
    Transmitted Power Density: 0.5 W/3mm = 70,000 W/m^2
    Return Power Density: 1e-34 W/m^2 = 0.00000000000000000000000000000000000000000000000000001 W/m^2
    '''
        now = datetime.datetime.now()
        tt=now.timetuple()
	(year,month,day,hour,min,sec,tm_wday,tm_yday,tm_isdst)=tt

	
	if float(self.distance)<10000:
		arrival_time=now+datetime.timedelta(0,float(self.distance)*365*24*3600)
		return_time=now+datetime.timedelta(0,float(self.distance)*365*24*3600*2)
		at=arrival_time.timetuple()
		rt=return_time.timetuple()
        	(ayear,amonth,aday,ahour,amin,asec,atm_wday,atm_yday,atm_isdst)=at
        	(ryear,rmonth,rday,rhour,rmin,rsec,rtm_wday,rtm_yday,rtm_isdst)=rt
	else:
		(ayear,amonth,aday,ahour,amin,asec,atm_wday,atm_yday,atm_isdst)=tt
        	(ryear,rmonth,rday,rhour,rmin,rsec,rtm_wday,rtm_yday,rtm_isdst)=tt
		ayear+=int(self.distance)
		ryear+=int(self.distance)*2	
	
        p=self.power(float(self.distance))

        e=-int(math.log10(p))
        m=p*10**e
        if not(__debug__): lpr =  subprocess.Popen("/usr/bin/lpr", stdin=subprocess.PIPE)

        things=["*****************",
        "Message: "+message,
        "Coded Message: "+coded_output,
       # "Date message sent: " +  now.strftime("%B %d, %Y %I:%M:%S %p"),
        "Date message sent:    " +  '{}-{:0>2d}-{:0>2d} {:0>2d}:{:0>2d}:{:0>2d}'.format(year,month,day,hour,min,sec,tm_wday,tm_yday,tm_isdst),
        "Message arrival date: " +  '{}-{:0>2d}-{:0>2d} {:0>2d}:{:0>2d}:{:0>2d}'.format(ayear,amonth,aday,ahour,amin,asec,atm_wday,atm_yday,atm_isdst),
        "Message return date:  " +  '{}-{:0>2d}-{:0>2d} {:0>2d}:{:0>2d}:{:0>2d}'.format(ryear,rmonth,rday,rhour,rmin,rsec,rtm_wday,rtm_yday,rtm_isdst),

        "Target "+self.star_type+": "+self.star]
        if (self.spectral_type): things.append("Spectral Type: "+self.spectral_type)
        things.extend([
        "Distance from Earth: "+"{:,}".format(float(self.distance)) + " light years",
        "Signal wavelength: 520 nm",
        "Outgoing Power Density: 161,290 W/m^2",
        "    or                  1.612e5 W/m^2",
        "Return Power Density: "+str(self.power(float(self.distance)))+" W/m^2",
        "    or                "+"0."+str(0)*e+str(int(m*1000))+" W/m^2",
        "Fun Fact: "+self.funfact,
        "*****************"
        ])
        output="\n".join(things)
        print output
        if not(__debug__): lpr.stdin.write(output)
        if not(__debug__): lpr.stdin.close()


if __name__ == "__main__":
    app = simpleapp_tk(None)
    app.title('my application')
    app.mainloop()
