from tkinter import ttk
import tkinter as tk

from ui.resizableframe import ResizableFrameRightEdge 
from ui.signalentry import SignalEntry
from ui.fileselector import FileSelector
from ui.collapsiblepanes import TogglePaneDel
from ui.collapsiblepanes import TogglePane
                
class PlotManager(tk.Frame):    
    def __init__(self, parent, presenter,*args,**kwargs)->None:
        """
        Initialize an instance of the class of PlotManager. 
        This is a control panel that manages the result files and signals.
        
        args: 
        - all the Frame arguments
            - background, bg: set background color
            - borderwidth, bd: set border width
            - ...
        
        -----USAGE-----
        This is used exactly as a Frame widget.
        """  
        super().__init__(parent,*args,**kwargs)
        
        self.toggleFrameList = []
        self.noOfRows = 0
        self.presenter = presenter
        
        # Set PlotManager columns weight
        self.columnconfigure(0,weight=1)

        # Results file selection
        self.noOfRows
        self.addPlot = ttk.Button(self,text='Add Plot',command = self.AddSubplot) 
        self.addPlot.grid(row=self.noOfRows,column=0,sticky='W')
    
    def AddSubplot(self)->None:
        '''Add a toggle frame to the plot manager pane.'''
        subplotLabel = "Subplot " + str(self.noOfRows)
        self.noOfRows += 1 
        self.toggleFrame = TogglePane(self, label = subplotLabel, bg = 'cyan')
        self.toggleFrame.grid(row = self.noOfRows, column = 0, sticky='EW')
        
        # Toggle pane content
        inputFileSelector = ResFileManager(self.toggleFrame.interior, self.presenter, bg = 'blue')
        inputFileSelector.grid(row=0,column=0,sticky='EW')



class ResFileManager(tk.Frame):
    def __init__(self, parent, presenter,*args,**kwargs)->None:
        """
        Initialize an instance of the class of ResFileManager. 
        This is a control panel that manages the result files and signals.
        
        args: 
        - all the Frame arguments
            - background, bg: set background color
            - borderwidth, bd: set border width
            - ...
        
        -----USAGE-----
        This is used exactly as a Frame widget.
        """  
        super().__init__(parent,*args,**kwargs)
        self.columnconfigure(0,weight=1)
        self.presenter = presenter
        self.noOfRows = 0
        addFileBtn = ttk.Button(self,text='Add Result File', command= self.AddResFile)
        addFileBtn.grid(row=self.noOfRows,column=0,sticky='W')
        
    def AddResFile(self)->None:
        '''Add result pane.'''
        self.noOfRows += 1
        self.resFilePane = ResFilePane(self, self.presenter)
        self.resFilePane.grid(row = self.noOfRows,column=0, sticky = 'EW')
        
        
        
class ResFilePane(tk.Frame):
    def __init__(self, parent, presenter,*args,**kwargs)->None:
        """
        UPDATE THIS
        Initialize an instance of the class of PlotManager. 
        This is a control panel that manages the result files and signals.
        
        args: 
        - all the Frame arguments
            - background, bg: set background color
            - borderwidth, bd: set border width
            - ...
        
        -----USAGE-----
        This is used exactly as a Frame widget.
        """  
        super().__init__(parent,*args,**kwargs)
        
        self.noOfRows = 0
        self.columnconfigure(0,weight=1)
        
        self.fileSelector = FileSelector(self,presenter, bg = 'grey40')
        self.fileSelector.grid(row=self.noOfRows,column=0,sticky='EW')
        
        self.noOfRows +=1
        self.signalCollection = ttk.Combobox(self,state='readonly')
        self.signalCollection.grid(row=self.noOfRows,column=0,sticky='EW', padx = 3, pady = 2)
        

        