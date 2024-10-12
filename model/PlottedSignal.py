from model.Signal import Signal

class PlottedSignals(Signal):
    def __init__(self,
                 lineThickness = 1,
                 lineStyle = '-',
                 marker = '',
                 color = [1, 1, 1],
                 *args,
                 **kwargs)->None:
        '''
        Class that generates the model of a PlottedSignals object.
        The purpose of this class is to store all the signals
        and related information contained in a subplot.
        '''
        super().__init__(*args,**kwargs)
        
        self.lineThickness = lineThickness 
        self.lineStyle = lineStyle
        self.marker = marker
        self.color = color
        