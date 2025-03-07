import tkinter as tk
from tkinter import ttk

class SubplotOptions(tk.Frame):
    def __init__(self,
                 parent,
                 presenter,
                 index,
                 title = '',
                 xLabel = '',
                 yLabel = '',
                 xLim = [0, 0],
                 yLim = [0, 0],
                 useUserLim = 0, 
                 xTick = 0,
                 yTick = 0,
                 useUserTicks = 0,
                 setGrid = 1,
                 *args,
                 **kwargs):
        
        ''' Initialize a subplot options pane.'''
        super().__init__(parent,*args,**kwargs)
        
        labelSize = 20
        btnSize = 10
        self.parent = parent
        self.presenter = presenter
        self.index = index
        self.useUserLim = useUserLim
        self.useUserTicks = useUserTicks
        self.setGrid = setGrid
        
        # Title frame
        rowNo = 0
        self.frame1 = tk.Frame(parent, pady=3)
        self.frame1.grid(row=rowNo,column=0, pady=3, sticky = 'NEW')
        self.frame1.columnconfigure(1,weight=1)
        
        self.titleLab = ttk.Label(self.frame1,text='Title',width=labelSize)
        self.titleLab.grid(row=0,column=0, pady=3)
        self.titleEntry = tk.Entry(self.frame1)
        self.titleEntry.grid(row=0,column=1,padx=3,sticky='EW')
        self.UpdateEntry(self.titleEntry, title)
        
        # X Axis labels frame
        rowNo +=1
        self.frame2 = tk.Frame(parent, pady=3)
        self.frame2.grid(row=rowNo,column=0, sticky = 'NEW')
        self.frame2.columnconfigure(1,weight=1)
        
        self.xAxisLabLab = ttk.Label(self.frame2, text = 'X Axis Label',width=labelSize)
        self.xAxisLabLab.grid(row=0,column=0)
        self.xAxisLabEntry = tk.Entry(self.frame2)
        self.xAxisLabEntry.grid(row=0,column=1,padx=3,sticky='EW')
        self.UpdateEntry(self.xAxisLabEntry, xLabel)
        
        # Y Axis labels frame
        rowNo +=1
        self.frame3 = tk.Frame(parent, pady=3)
        self.frame3.grid(row=rowNo,column=0, sticky = 'NEW')
        self.frame3.columnconfigure(1,weight=1)
        self.yAxisLabLab = ttk.Label(self.frame3, text = 'Y Axis Label',width=labelSize)
        self.yAxisLabLab.grid(row=1,column=0)
        self.yAxisLabEntry = tk.Entry(self.frame3)
        self.yAxisLabEntry.grid(row=1,column=1,padx=3,sticky='EW')
        self.UpdateEntry(self.yAxisLabEntry, yLabel)
                
        # X Axis limits frame
        rowNo +=1
        self.frame4 = tk.Frame(parent, pady=3)
        self.frame4.grid(row=rowNo,column=0, sticky = 'NEW')
        
        self.xAxisLimLab = ttk.Label(self.frame4, text = 'X Axis Limits',width=labelSize)
        self.xAxisLimLab.grid(row=0,column=0)
        
        self.xAxisLowLimEntry = tk.Entry(self.frame4)
        self.xAxisLowLimEntry.grid(row=0,column=1,padx=3)
        self.UpdateEntry(self.xAxisLowLimEntry, str(xLim[0]))
        
        self.xAxisUpLimEntry = tk.Entry(self.frame4)
        self.xAxisUpLimEntry.grid(row=0,column=2,padx=3)    
        self.UpdateEntry(self.xAxisUpLimEntry, str(xLim[1]))
        
        self.xAxisLowLimEntry.bind("<FocusOut>",lambda event: self.ValidateLowLimEntries(event, self.xAxisUpLimEntry, str(xLim[0])))
        self.xAxisLowLimEntry.bind("<Return>",lambda event: self.ValidateLowLimEntries(event, self.xAxisUpLimEntry, str(xLim[0])))
        self.xAxisUpLimEntry.bind("<FocusOut>",lambda event: self.ValidateUpLimEntries(event, self.xAxisLowLimEntry, str(xLim[1])))
        self.xAxisUpLimEntry.bind("<Return>",lambda event: self.ValidateUpLimEntries(event, self.xAxisLowLimEntry, str(xLim[1])))
        
        # Y Axis limits frame
        rowNo +=1
        self.frame5 = tk.Frame(parent, pady=3)
        self.frame5.grid(row=rowNo,column=0, sticky = 'NEW')
        
        self.yAxisLimLab = ttk.Label(self.frame5, text = 'Y Axis Limits',width=labelSize)
        self.yAxisLimLab.grid(row=1,column=0)
        
        self.yAxisLowLimEntry = tk.Entry(self.frame5)
        self.yAxisLowLimEntry.grid(row=1,column=1,padx=3)
        self.UpdateEntry(self.yAxisLowLimEntry, str(yLim[0]))
        
        self.yAxisUpLimEntry = tk.Entry(self.frame5)
        self.yAxisUpLimEntry.grid(row=1,column=2,padx=3)
        self.UpdateEntry(self.yAxisUpLimEntry, str(yLim[1]))
        
        self.yAxisLowLimEntry.bind("<FocusOut>",lambda event: self.ValidateLowLimEntries(event, self.yAxisUpLimEntry, str(yLim[0])))
        self.yAxisLowLimEntry.bind("<Return>",lambda event: self.ValidateLowLimEntries(event, self.yAxisUpLimEntry, str(yLim[0])))
        self.yAxisUpLimEntry.bind("<FocusOut>",lambda event: self.ValidateUpLimEntries(event, self.yAxisLowLimEntry, str(yLim[1])))
        self.yAxisUpLimEntry.bind("<Return>",lambda event: self.ValidateUpLimEntries(event, self.yAxisLowLimEntry, str(yLim[1])))

        # X Axis Ticks
        rowNo +=1
        self.frame6 = tk.Frame(parent, pady=3)
        self.frame6.grid(row=rowNo,column=0, sticky = 'NEW')
        self.xAxisTicksLab = ttk.Label(self.frame6, text = 'X Axis Ticks',width=labelSize)
        self.xAxisTicksLab.grid(row=1,column=0)
        self.xAxisTicksEntry = tk.Entry(self.frame6)
        self.xAxisTicksEntry.grid(row=1,column=1,padx=3)
        self.UpdateEntry(self.xAxisTicksEntry, str(xTick))
        self.xAxisTicksEntry.bind("<FocusOut>", lambda event: self.ValidateTicksEntry(event,str(xTick)))
        self.xAxisTicksEntry.bind("<Return>", lambda event: self.ValidateTicksEntry(event,str(xTick)))
        
                    
        # Y Axis Ticks
        rowNo +=1
        self.frame7 = tk.Frame(parent, pady=3)
        self.frame7.grid(row=rowNo,column=0, sticky = 'NEW')
        self.yAxisTicksLab = ttk.Label(self.frame7, text = 'Y Axis Ticks',width=labelSize)
        self.yAxisTicksLab.grid(row=1,column=0)
        self.yAxisTicksEntry = tk.Entry(self.frame7)
        self.yAxisTicksEntry.grid(row=1,column=1,padx=3)
        self.UpdateEntry(self.yAxisTicksEntry, str(yTick))
        self.yAxisTicksEntry.bind("<FocusOut>", lambda event: self.ValidateTicksEntry(event,str(yTick)))
        self.yAxisTicksEntry.bind("<Return>", lambda event: self.ValidateTicksEntry(event,str(yTick)))
        
        # Set Use User Limits
        rowNo +=1
        self.userLimFrame = tk.Frame(parent, pady=3)
        self.userLimFrame.grid(row=rowNo,column=0, sticky = 'NEW')
        
        self.gridLab = ttk.Label(self.userLimFrame, text = 'Set Axis Limits',width=labelSize)
        self.gridLab.grid(row=0,column=1)
        self.userLimVar = tk.DoubleVar(value=useUserLim)
        
        self.userLimCheckbox = ttk.Checkbutton(self.userLimFrame,variable=self.userLimVar, command = self.SetLimEntryState)
        if self.userLimVar.get() == True:
            self.userLimCheckbox.state(['selected'])
        else:
            self.userLimCheckbox.state(['!selected'])
        self.userLimCheckbox.grid(row=0,column=2)
        
        self.SetLimEntryState()
        
        # Set Use User Ticks
        rowNo +=1
        self.userTicksFrame = tk.Frame(parent, pady=3)
        self.userTicksFrame.grid(row=rowNo,column=0, sticky = 'NEW')
        
        self.userTicksLab = ttk.Label(self.userTicksFrame, text = 'Set Axis Ticks',width=labelSize)
        self.userTicksLab.grid(row=0,column=1)
        self.userTicksVar = tk.DoubleVar(value=self.useUserLim)
        
        self.userTicksCheckbox = ttk.Checkbutton(self.userTicksFrame,variable=self.userTicksVar,command = self.SetTicksEntryState)
        if  self.userTicksVar.get() == True:
            self.userTicksCheckbox.state(['selected'])
        else:
            self.userTicksCheckbox.state(['!selected'])
        self.userTicksCheckbox.grid(row=0,column=2)
        self.SetTicksEntryState()
        
        # Grid frame
        rowNo +=1
        self.gridFrame = tk.Frame(parent, pady=3)
        self.gridFrame.grid(row=rowNo,column=0, sticky = 'NEW')
        
        self.gridLab = ttk.Label(self.gridFrame, text = 'Grid',width=labelSize)
        self.gridLab.grid(row=0,column=1)
        
        self.gridVar = tk.DoubleVar(value=self.setGrid)
        self.gridCheckbox = ttk.Checkbutton(self.gridFrame,variable=self.gridVar)
        if self.gridVar.get() == True:
            self.gridCheckbox.state(['selected'])
        else:
            self.gridCheckbox.state(['!selected'])
        self.gridCheckbox.grid(row=0,column=2)
        
        # Button frame
        rowNo +=1
        btnFrame = tk.Frame(parent, pady=5)
        btnFrame.grid(row=rowNo,column=0, sticky = 'NEW')
        btnFrame.columnconfigure(0,weight=1)
        
        cancelBtn = ttk.Button(btnFrame,text = 'Cancel', width = btnSize, command=lambda:self.presenter.CloseSubplotOptions(self))
        cancelBtn.grid(row = 0, column=0, sticky = 'E')
        applyBtn = ttk.Button(btnFrame,text = 'Apply', width = btnSize, command=lambda:self.presenter.ApplySubplotOptions(self))
        applyBtn.grid(row = 0, column=1, sticky = 'E')
        okBtn = ttk.Button(btnFrame,text = 'Ok', width = btnSize, command=lambda:self.presenter.OkSubplotOptions(self))
        okBtn.grid(row = 0, column=2, sticky = 'E')
        
        
    def UpdateEntry(self,entry:ttk.Entry,txt:str)->None:
        """This function takes whatever entry, deleted the text, and write the new 
        text given as input. """
        # Delete and rewrite the entry text 
        entry.delete(0,tk.END)
        entry.insert(0,txt)
        
    def SetLimEntryState(self)->None:
        '''Set the state of the user limits entries.'''
        
        if self.userLimVar.get():
            self.yAxisLowLimEntry.config(state="normal")
            self.yAxisUpLimEntry.config(state="normal")
            self.xAxisLowLimEntry.config(state="normal")
            self.xAxisUpLimEntry.config(state="normal")
            
        else:
            self.yAxisLowLimEntry.config(state="disabled")
            self.yAxisUpLimEntry.config(state="disabled")
            self.xAxisLowLimEntry.config(state="disabled")
            self.xAxisUpLimEntry.config(state="disabled")
            
    def SetTicksEntryState(self)->None:
        '''Set the state of the user ticks entries.'''
        a = self.userTicksVar.get()
        if self.userTicksVar.get():
            self.xAxisTicksEntry.config(state="normal")
            self.yAxisTicksEntry.config(state="normal")
            
        else:
            self.xAxisTicksEntry.config(state="disabled")
            self.yAxisTicksEntry.config(state="disabled")
            
    def ValidateUpLimEntries(self,event,otherLimit, previousVal)->None:
        '''Validate entries.'''
        # Check if the entry is a number, and if it is right with respect to 
        # its counterpart
        print("validate")
        try:
            currentEntry = float(event.widget.get())
            otherEntry = float(otherLimit.get())
            
            if currentEntry<=otherEntry:
                self.UpdateEntry(event.widget,previousVal)
        except:
            self.UpdateEntry(event.widget,previousVal)
                      
    def ValidateLowLimEntries(self,event,otherLimit, previousVal)->None:
        '''Validate entries.'''
        # Check if the entry is a number, and if it is right with respect to 
        # its counterpart
        try:
            currentEntry = float(event.widget.get())
            otherEntry = float(otherLimit.get())
            
            if currentEntry>=otherEntry:
                self.UpdateEntry(event.widget,previousVal)
        except:
            self.UpdateEntry(event.widget,previousVal)
                        
    def ValidateTicksEntry(self,event, previousVal)->None:
        '''Validate the ticks entry.'''
        try:
            currentEntry = float(event.widget.get())
            if currentEntry <= 0:
                self.UpdateEntry(event.widget,previousVal)
        except:
            self.UpdateEntry(event.widget,previousVal)
            
            
