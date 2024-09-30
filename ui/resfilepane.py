from tkinter import ttk
import tkinter as tk
from ui.signalpane import SignalPane
from ui.fileselector import FileSelectorDel

class ResFilePane(tk.Frame):
    def __init__(self, parent, presenter,*args,**kwargs)->None:
        """
        Initialize an instance of the class of ResFilePane. 
        This is a pane where, given a result file, signals can be selected.
        
        args: 
        - all the Frame arguments
            - background, bg: set background color
            - borderwidth, bd: set border width
            - ...
        
        -----USAGE-----
        This is used exactly as a Frame widget.
        """  
        super().__init__(parent,*args,**kwargs)
        # Set columns weight
        self.columnconfigure(0,weight=1)
        
        # Handy numbers
        self.name = ''
        self.indx = 0
        self.noOfRows = 0
        self.presenter = presenter
        
        self.fileSelector = FileSelectorDel(self,presenter, bg = 'grey40')
        self.fileSelector.grid(row=self.noOfRows,column=0,sticky='EW')
        
        self.noOfRows +=1
        listOfSignals = ["Option 1", "Option 2", "Option 3"]
        self.signalCollection = ttk.Combobox(self,state='readonly', values=listOfSignals)
        self.signalCollection.grid(row=self.noOfRows,column=0,sticky='EW', padx = 3, pady = 2)
        
        self.signalCollection.bind("<<ComboboxSelected>>", self.PrintCombo)
        
    def PrintCombo(self,event):
        '''Test fun'''
        selection = self.signalCollection.get()
        
        self.noOfRows +=1
        sigPane = SignalPane(self, self.presenter, sigName = selection, bg = 'red')
        sigPane.grid(row=self.noOfRows,column=0,sticky='EW')
        
    