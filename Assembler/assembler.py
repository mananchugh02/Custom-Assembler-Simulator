
from utils import getBin8Bits
from Float_to_IEEE import final
from errorHandler import ErrorHandler
class Assembler:
    def __init__(self,regAddr,instructionTypeDict,unusedBitsDict):
        self.regAddrTable = regAddr
        self.isaInstructions = instructionTypeDict
        self.variableTable = {}
        self.labesTable = {}
        self.locationCounter = 0
        self.raw_input = []
        self.output = []
        self.processedInput=[]
        self.variableCount =0 
        self.unusedBitsTable = unusedBitsDict
        self.errorHandler = ErrorHandler()
        
    def pass1 (self):
        for index,line in enumerate(self.raw_input):
            if (line[0] == 'var'):
                if(index -1 >= 0 and self.raw_input[index - 1][0] != "var"):
                    self.errorHandler.handle(7)
                self.variableTable[line[1]] = self.variableCount
                self.variableCount+=1
                continue
            if (line[0][-1] == ":"):
                self.labesTable[line[0][:-1]] = self.locationCounter
                if( len(line) == 2):
                    continue
                else:
                    line = line[1:]
            self.locationCounter+=1
            self.processedInput.append(line)
        self.errorHandler.varlist = self.variableTable.keys()
        self.errorHandler.label_list = self.labesTable.keys()
        if(len(set(self.errorHandler.label_list).intersection(set(self.errorHandler.varlist))) != 0):
            return self.errorHandler.handle(6,8)
        if(len(set(self.regAddrTable.keys()).intersection(self.variableTable.keys())) != 0):
            return self.errorHandler.handle(11,1)
    def setRawInput(self,inp):
        self.raw_input = inp       
    def pass2(self):
        for line in self.processedInput:
            # print(line)
            if(self.errorHandler.errorCheck(line) == -1):
                continue
            opcode = self.isaInstructions[line[0]]
            if line[0] == "mov":
                if "$" in line[2]:
                    opcode = opcode[0]
                elif line[2] in self.regAddrTable.keys():
                    opcode = opcode[1]
                else:
                    pass 
                    #Error
            binary = opcode[0]+ "0"* self.unusedBitsTable[opcode[1]]
            for ins in line[1:]:
            
                if type(ins) == int:
                    continue
                if ins in self.regAddrTable.keys():
                    binary = binary + self.regAddrTable[ins]
                    continue
                elif "$" in ins:
                    if line[0][-1] == 'f':
                        binary+=final(float(ins.split("$")[1]))[0]
                    else:
                        binary+= getBin8Bits(int(ins.split("$")[1]),"imm")
                elif  ins in self.labesTable.keys():
                    binary+= getBin8Bits(self.labesTable[ins],"mem")
                elif ins in self.variableTable.keys():
                    binary+= getBin8Bits( self.locationCounter + self.variableTable[ins],"mem")
            self.output.append(binary)
                
        
    def compile(self):
        self.pass1()
        if (self.errorHandler.errorState ==1):
            return
        self.pass2()
        return self.output