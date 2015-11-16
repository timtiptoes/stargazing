#!/usr/bin/python



import csv
import time
import datetime
import Tkinter
import subprocess
import math


class simpleapp_tk():


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

    factor=1


    #What to do when user presses OK
    def __init__(self):
        input="e"
          #    1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890
        self.factor=100
        (self.factor,self.audio_dot,self.audio_dash) = get_speed_factors(input)

        coded_output=""
        for letter in input:
            print letter*20
            if (letter == ' '):
                display_string = "<space>"
                time.sleep(7*self.factor)
                coded_output+=" "
            else:
                coded_output+=self.CODE[letter.upper()]+" "
                display_string = letter + ":   "
            for symbol in self.CODE[letter.upper()]:
                if symbol == '-':
                    display_string+="-"
                    self.dash()
                elif symbol == '.':
                    self.dot()
                else:
                    time.sleep(0.5*self.factor)
            print "inter character gap"
            time.sleep(3*self.factor)
            print "-------------"
        print "message sent: "+coded_output



    def dot(self):
        print "dot"
        print "open shutter"
        subprocess.call(["cvlc", "--play-and-exit", "/home/tim/github/stargazing/data/dot.wav"])
        time.sleep(self.factor)
        print "close shutter"
        time.sleep(self.factor)

    def dash(self):
        print "dash"
        print "shutter open"
        subprocess.call(["amixer","-D", "pulse", "sset", "Master", "4%"])

        subprocess.call(["cvlc", "--play-and-exit", "/home/tim/github/stargazing/data/dash.wav"])
        time.sleep(3*self.factor)
        print "shutter closed"
        time.sleep(self.factor)

    def get_speed_factors(input):
        if (len(input)<=10):
            return (1,'audiocheck.net_sin_800Hz_-3dBFS_1.0s.wav','audiocheck.net_sin_800Hz_-3dBFS_3s.wav')
        elif (len(input)<=50):
            return(0.5,'audiocheck.net_sin_800Hz_-3dBFS_0.5s.wav','audiocheck.net_sin_800Hz_-3dBFS_1.5s.wav')
        else:
            return(0.1,'audiocheck.net_sin_800Hz_-3dBFS_0.1s.wav','audiocheck.net_sin_800Hz_-3dBFS_0.3s.wav')



if __name__ == "__main__":
    app = simpleapp_tk()
