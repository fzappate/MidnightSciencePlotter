class SubplotModel():
    def __init__(self)->None:
        '''
        Class that generates the model of a Subplot.
        The purpose of this class is to store all the 
        information necessary to draw a subplot.
        '''
        # Dictionary with signal names and values
        self.indx = 0
        self.noOfResFile = 0
        self.resultFiles = []
        self.plottedSignals = []
        self.xAxisSignals = []
        self.xAxisSignalsName = []
        self.xAxisSelected = []
        self.xAxisSelectedIndx = 0 
        self.xAxisSelectedName = '' # TO BE DELETED
        
        self.name = ''
        self.xLabel = ''
        self.yLabel = ''
        self.xLim = [0, 1]
        self.yLim = [0, 1]
        self.xLimUser = [0, 0]
        self.yLimUser = [0, 0]
        self.useUserLim = False
        self.xTick = 0.2
        self.yTick = 0.2
        self.xTickUser = 0.0
        self.yTickUser = 0.0
        self.setGrid = True
        # self.xAxis = ''
        
    def AddResultFile(self,resultFileModel):
        '''Add ResultFileModel to SubplotModel.'''
        self.resultFiles.append(resultFileModel)
        self.noOfResFile = len(self.resultFiles)
        
    def DeleteResultFile(self,resultFilePane):
        '''Remove a ResultFileModel from SubplotModel.'''
        # Remove result file
        resultFileNo = resultFilePane.indx
        del self.resultFiles[resultFileNo]
        
        # Reassign result files indx
        for ii, resFileTemp in enumerate(self.resultFiles):
            resFileTemp.indx = ii
            
        self.noOfResFile = len(self.resultFiles)
        
        
        
        