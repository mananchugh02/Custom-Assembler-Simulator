import sys;
from input_module import get_raw_file
import asm as asmData
from assembler import Assembler
# print(sys.argv)
input_file =  "a.in" if len(sys.argv) < 2 else sys.argv[1]
output_file = "a.out" if len(sys.argv) < 3 else sys.argv[2]

# print(inp)
asm = Assembler(asmData.Reg_Adress,asmData.ISA_Dict,asmData.unUsedBitsTable)
inp = get_raw_file(input_file,asm)
# print(asm.errorHandler.errorState)
asm.setRawInput(inp)
output = asm.compile()
# print(asm.labesTable)
# print(*asm.processedInput,sep="\n")
# print(asm.errorHandler.errorState)
if(asm.errorHandler.errorState != 0):
    sys.stdout.write("Compilation not done due to errors\n")
else:
    sys.stdout.writelines(map( lambda x : x+"\n", asm.output ))
