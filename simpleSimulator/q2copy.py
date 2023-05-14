from sys import stdin
from Decode import Decoder
from execute import SIM
import simDicts
from utils import getBin8Bits,final
from plot_graph import plot_graph
Mem= [0]*256
i = 0 
for line in stdin:
    if i > 255:
        continue
    if line.strip() == '':
        i+=1    
        continue
    Mem[i] = line.strip()
    i+=1
    def dectobin(dec):
        j=""
        while dec>0:
            k=dec%2
            dec=dec//2
            k=str(k)
            j=j+k
        j=j[::-1]
        j=str(j)
        result=""
        result+="0"*(16-len(j))
        result+=j
        return result[-16:]
def encodeNum(num):
    if type(num) == int:
        return dectobin(num)
    else:
        return final(num)[0]
def dumpreg(i):
    
    for m,v in simDicts.reg_in.items():
            if m == None:
                continue
            k = encodeNum(v)
            if len(k) == 8:
                print("0"*8 + k,end=" ")
            else:
                print(k,end=" ")
def dumpMem(i):
    for m in Mem:
        if m == None:
            print("0"*16)
            continue
        if type(m) == str:
            print(m)
            continue
        k = encodeNum(m)
        if len(k) == 8:
            print("0"*8 + k)
        else:
            print(k)
dec = Decoder(simDicts.isa_dict,simDicts.unUsedBitsTable,simDicts.isa_names,simDicts.reg_in)
ex =SIM(simDicts.reg_in,Mem)
pc = 0
i = 0
while (ex.halted == 0):
    print(getBin8Bits(pc,1),end= " ")
    ex.mem_addr.append(pc)
    ex.arr = dec.decode(Mem[pc])
    ex.cycle.append(i)
    dumpreg(i)
    simDicts.reg_in = ex.reg_in
    print()
    i+=1
dumpMem(i)
plot_graph(ex.cycle,ex.mem_addr)