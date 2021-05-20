import tkinter as tk
import threading
from tkinter import Button, messagebox

from pandastable.plotting import TkOptions

#from webFuncs import *
import pandas as pd
from pandastable import Table
import time
import webbrowser

#class App(threading.Thread):
#    
#    def __init__(self,df):
#        threading.Thread.__init__(self,None)
#        self.start()
#        self.df = df
#
#    def callback(self):
#        self.root.quit()
#
#    def run(self):
#        self.root = tk.Tk()
#        self.root.protocol("WM_DELETE_WINDOW", self.callback)
#
#        self.root.title('Kortletarna')
#        frame = tk.Frame(self.root)
#        frame.pack()
#        pt = Table(frame, dataframe=df)
#        pt.show()
#
#        self.root.mainloop()
#    
#    def getdf(self):
#        return self.df
def stockTrue(url, name):
    #Do something, like opening up a popup with link
    root = tk.Tk()
    root.geometry("175x100")
    text1 = tk.Label(root,text="Du hittade ett grafikkort:")
    text2 = tk.Label(root,text=name)
    text3 = tk.Label(root,text="Vill du öppna länken?")
    open = Button(root, text ="Öppna länk", command = lambda: do(url,root))
    close = Button(root, text="Skippa", command=root.destroy)

    text1.pack()
    text2.pack()
    text3.pack()
    open.pack()
    close.pack()
    root.mainloop()
    return
    
def do(url,root):
    webbrowser.open(url)
    root.destroy()
    return



#df = pd.DataFrame({
#            '': ['GTX 3060','GTX 3070','GTX 3080'],
#            'Webhallen': ['Letar...','Ej implementerat','Ej implementerat'],
#            'Proshop': ['Letar...','Ej implementerat','Ej implementerat'],
#            'Inet': ['Letar...','Ej implementerat','Ej implementerat'],
#        })
#app = App(df)

#startChecking()


#root.iconbitmap("/monke.ico")

# Showing it onto the screen
#rubrik.pack()
#status_log.pack()
#root.after(2000, startChecking())