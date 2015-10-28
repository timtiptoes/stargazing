__author__ = 'timtiptoes'
#Taken from https://books.google.com/books?id=JnR9hQA3SncC&pg=PA414&dq=python+tk+images&hl=en&sa=X&ved=0CB0Q6AEwAGoVChMIjLSZsd-wyAIVwjeICh1fqQKR#v=onepage&q=python%20tk%20images&f=false
import os
import Tkinter

root=Tkinter.Tk()
L=Tkinter.Listbox(selectmode=Tkinter.SINGLE)
gifsdict={}

dirpath='/Users/timtiptoes/Dropbox/tims_stuff/Professional/companies/companies 2013/AMAT/AMAT/Final_file_extract_9_7_04/administravia/Online Credit Reports_files'
for gifname in os.listdir(dirpath):
    #if not gifname[0].isdigit(): continue
    gifpath=os.path.join(dirpath, gifname)
    gif=Tkinter.PhotoImage(file=gifpath)
    gifsdict[gifname]=gif
    L.insert(Tkinter.END,gifname)

L.pack()
img=Tkinter.Label()
img.pack()
def list_entry_clicked(*ignore):
    imgname=L.get(L.curselection()[0])
    img.config(image=gifsdict[imgname])
L.bind('<ButtonRelease-1>', list_entry_clicked)
root.mainloop()