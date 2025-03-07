import tkinter as tk
from tkinter import ttk 

# Important order of import
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt

import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk
        
class PlotCanvas(tk.Frame):
    '''Class of plot where the GearGen gear set is plot.'''

    def __init__(self,parent,*args, **kwargs)->None:
        '''Initialize the PlotUI object.'''
        super().__init__(parent,*args, **kwargs)
                
        self.columnconfigure(0,weight=1)
        self.rowconfigure(0,weight=1)
        
        # Create a blank canvas to start
        self.fig, axs = plt.subplots(1)
        # self.fig.subplots_adjust(left=0.05, bottom=0.05, right=0.95, top=0.95, wspace=0.1, hspace=0.2)
        
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.toolbar = NavigationToolbar2Tk(self.canvas, self)
        self.toolbar.update()
        self.toolbar.pack(side=tk.TOP, fill=tk.BOTH, expand=False)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
               
        
    def DeleteSubplot(self):
        '''
        Remove subplot.
        '''





