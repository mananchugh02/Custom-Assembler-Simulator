from math import log2
space_mem = input("Input memory space : ")
type_addresable = input("Input addressable memory type : ")
y=space_mem[-5:]
if space_mem[-2:] == "mB":
    space_mem = int(space_mem[:-2])*((2**20)*8)
elif space_mem[-2:] == "mb":
    space_mem = int(space_mem[:-2])*((2**20))
elif space_mem[-2:] == "kB":
    space_mem = int(space_mem[:-2])*((2**10)*8)
elif space_mem[-2:] == "kb":
    space_mem = int(space_mem[:-2])*((2**10))
elif space_mem[-2:] == "kN":
    space_mem = int(space_mem[:-2])*((2**10)*4)
elif space_mem[-2:] == "mN":
    space_mem = int(space_mem[:-2])*((2**20)*4)
elif space_mem[-5:] == "kWord":
    space_mem = int(space_mem[:-5])*((2**10))
elif space_mem[-5:] == "mWord":
    space_mem = int(space_mem[:-5])*((2**20))
d = {
    "Byte":8,
    "Bit":1,
    "Nibble":4,
    "Word":1
}
mem_slots = space_mem/d[type_addresable]
bits_required = log2(mem_slots)
query_type = int(input("""Input the type of question (1/2)\n1. ISA TYPE\n2. Enhancement Type"""))
if query_type == 1:
    lenofins = int(input("Input the length of 1 instruction : "))
    lenofreg = int(input("Input the length of registers : "))
    print("Bits required to represent an address is : ",bits_required)
    q = lenofins-lenofreg-bits_required
    print("Bits needed by opcode : ",q)
    print("Filler bits in instruction type 2 : ",lenofins-2*lenofreg-q)
    M_I=2**q
    print("Maximum number of instructions this ISA can support : ",M_I)
    M_R=2**lenofreg
    print("Maximum number of registers this ISA can support : ",M_R)
else:
    x=int(input("Enter the Sub-Type (1/2) : "))
    if x==1:
        cpu_bit = int(input("How many bits the cpu is : "))
        new_type_addresable = input("Input the New addressable memory type : ")
        d['Word']=cpu_bit
        if(y=='kWord' or y=='mWord'):
            space_mem=space_mem*cpu_bit
            mem_slots=space_mem/d[type_addresable]
            bits_required=log2(mem_slots)
        mem_slots_new=space_mem/d[new_type_addresable]
        bits_reqd_new=log2(mem_slots_new)
        otpt=bits_reqd_new-bits_required
        flag=0
        print(otpt)
        if(otpt<0):
            flag=1
        if flag==1:
            print(abs(otpt),"Pins saved")
        elif flag==0:
            print(abs(otpt),"Pins required")
    elif x==2:
        cpu_bit = int(input("How many bits is the CPU ? : "))
        pins= int(input("Enter the address pins : "))
        new_type_addresable = input("Input new addressable memory type : ")
        d['Word']=cpu_bit
        if(new_type_addresable=='Word'):
            d['Word']=cpu_bit
        total=(2**pins)*d[new_type_addresable]/8
        final=total/(2**30)
        print(final,' GB')