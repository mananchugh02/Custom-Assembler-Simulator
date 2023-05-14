import IEEE_TO_FLOAT
class Decoder:
    def __init__(self, isa_dict, unUsedBitsTable, isa_names, reg_in):
        self.isa_dict = isa_dict
        self.unUsedBitsTable = unUsedBitsTable
        self.isa_names = isa_names
        self.reg_in = reg_in


    def decodeNum(self, formatted_num):
        n = len(formatted_num)
        s = 0
        formatted_num = formatted_num[::-1]
        for i in range(n):

            s += (int(formatted_num[i])*(2**i))
        return s
    def bin2dec(self,formatted_num):
        n = len(formatted_num)
        s = 0
        formatted_num = formatted_num[::-1]
        for i in range(n):

            s += (int(formatted_num[i])*(2**i))
        return s
    def decode(self, instruction):
        opcode = instruction[0:5]
        type = self.isa_dict[opcode]
        func = self.isa_names[opcode]
        a = []
        a.append(func)
        if(type == "A"):
            r1 = instruction[7:10]
            r2 = instruction[10:13]
            r3 = instruction[13:16]
            v1 = self.reg_in[r1]
            v2 = self.reg_in[r2]
            a.append(v1)
            a.append(v2)
            a.append(r3)
        elif(type == 'B'):
            r1 = instruction[5:8]
            imm = instruction[8:16]
            if func == "movf":
                # print(imm)
                imm = IEEE_TO_FLOAT.final(imm)
            else:
                imm = self.decodeNum(imm)
            a.append(r1)
            a.append(imm)
        elif(type == 'C'):
            if(func == 'div'):
                r1 = instruction[10:13]
                r2 = instruction[13:16]
                v1 =  self.reg_in[r1]
                v2 =  self.reg_in[r2]
                a.append(v1)
                a.append(v2)
            elif (func== 'not'):
                r1 = instruction[10:13]
                r2 = instruction[13:16]
                v1 =  self.reg_in[r1]
                v2 =  self.reg_in[r2]
                a.append(v1)
                a.append(r2)
            else:
        
                r1 = instruction[10:13]
                r2 = instruction[13:16]
                v1 =  self.reg_in[r1]
                if func == "mov"  or func == "movf":
                    a.append(r2)
                    a.append(v1)
                else:
                    a.append(v1)
                    a.append(r2)
        elif(type == 'D'):

            r1 = instruction[5:8]
            madd = instruction[8:16]
            a.append(r1)
            a.append(madd)
        elif(type =='E'):
            madd = instruction[8:16]
            
            a.append(self.bin2dec(madd))
                      
        return a
    
# #1010100100000111
# a = ["mul",5,"00000111"]