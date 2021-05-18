import tkinter as tk
import threading
from tkinter import messagebox

from pandastable.plotting import TkOptions
from stockChecker import *
#from webFuncs import *
import pandas as pd
from pandastable import Table
import time
import webbrowser

class App(threading.Thread):
    
    def __init__(self,df):
        threading.Thread.__init__(self,None)
        self.start()
        self.df = df

    def callback(self):
        self.root.quit()

    def run(self):
        self.root = tk.Tk()
        self.root.protocol("WM_DELETE_WINDOW", self.callback)

        self.root.title('Kortletarna')
        frame = tk.Frame(self.root)
        frame.pack()
        pt = Table(frame, dataframe=df)
        pt.show()

        self.root.mainloop()
    
    def getdf(self):
        return self.df
    def stockTrue(self, url, name):
        #Do something, like opening up a popup with link
        response = messagebox.askquestion("I lager","Du hittade ett grafikkort! Vill du öppna länken?")
        if response == "yes":
            #Open url
            webbrowser.open(url)
            return
        elif response == "no":
            #close popup and resume rest of the code
            return
        return
    



df = pd.DataFrame({
            '': ['GTX 3060','GTX 3070','GTX 3080'],
            'Webhallen': ['Letar...','Ej implementerat','Ej implementerat'],
            'Proshop': ['Letar...','Ej implementerat','Ej implementerat'],
            'Inet': ['Letar...','Ej implementerat','Ej implementerat'],
        })
app = App(df)

startChecking(app)


#root.iconbitmap("/monke.ico")

# Showing it onto the screen
#rubrik.pack()
#status_log.pack()
#root.after(2000, startChecking())