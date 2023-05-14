from utils import final
class SIM:
    def __init__(self,reg_in,mem,arr=[]):
        self.arr=arr
        self.n=len(arr)
        self.halted=0
        self.reg_in=reg_in
        self.mem = mem
        self.mem_addr = []
        self.cycle = []
    def decodeNum(self,formatted_num):
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
    def dectobin(self,dec):
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
    def execute(self,PC):
        if(self.arr[0]=='add'):
            self.reg_in["111"] = 0
            a=self.arr[1]
            b=self.arr[2]
            c=""
            if a + b > 65535:
                self.reg_in["111"] = 8
                a = self.dectobin(a+b)
                b =0 
                a = self.bin2dec(a)
                
            c=a+b
            self.reg_in[self.arr[3]]=c    
            PC+=1
        elif(self.arr[0]=='addf'):
            self.reg_in["111"] = 0
            a=self.arr[1]
            b=self.arr[2]
            if type(a) == int:
                a =self.dectobin(a)[-16:]
                a = self.bin2dec(a)
            if type(b) == int:
                b =self.dectobin(b)[-16:]
                b = self.bin2dec(b)
            c=""
            c,f = final(a + b)
            if f==1:
                self.reg_in["111"] = 8
                self.reg_in[self.arr[3]]= float(252)   
                return PC + 1
                
            c=a+b
            self.reg_in[self.arr[3]]=c    
            PC+=1
        elif(self.arr[0]=='sub'):
            self.reg_in["111"] = 0
            a=self.arr[1]
            b=self.arr[2]
            if a - b < 0:
                self.reg_in["111"] = 8
                a = self.dectobin(a-b)
                b =0 
                a = self.bin2dec(a)
            c=""
            c=a-b
            self.reg_in[self.arr[3]]=c 
            PC+=1
        elif(self.arr[0]=='subf'):
            self.reg_in["111"] = 0
            a=self.arr[1]
            b=self.arr[2]
            if type(a) == int:
                a =self.dectobin(a)[-16:]
                a = self.bin2dec(a)
            if type(b) == int:
                b =self.dectobin(b)[-16:]
                b = self.bin2dec(b)
            c=""
            if a - b < 0 :
                self.reg_in["111"] = 8
                c = float(1)
                self.reg_in[self.arr[3]]=c    
                return PC + 1
                
            c=a-b
            self.reg_in[self.arr[3]]=c    
            PC+=1
        elif(self.arr[0]=='mov' or self.arr[0]=='movf' ):                 
            self.reg_in["111"] = 0
            b=""
            b=self.arr[2]
            self.reg_in[self.arr[1]]=b
            PC+=1
        elif(self.arr[0]=='ld'):                 #mem adress data do in binary
            self.reg_in["111"] = 0
            self.cycle.append(self.cycle[-1])
            self.mem_addr.append(self.bin2dec(self.arr[2]))
            self.reg_in[self.arr[1]] = self.mem[self.bin2dec(self.arr[2])]
            PC+=1
        elif(self.arr[0]=='st'):
            self.reg_in["111"] = 0
            self.cycle.append(self.cycle[-1])
            self.mem_addr.append(self.bin2dec(self.arr[2]))
            self.mem[self.bin2dec(self.arr[2])]=self.reg_in[self.arr[1]]
            PC+=1
            
        elif(self.arr[0]=='mul'):
            self.reg_in["111"] = 0
            a=self.arr[1]
            b=self.arr[2]
            c=""
            if a*b > 65535:
                self.reg_in["111"] = 8
                a = self.dectobin(a*b)
                b = 1
                a = self.bin2dec(a)
            c=a*b
            self.reg_in[self.arr[3]]=c
            PC+=1
        elif(self.arr[0]=='div'):
            self.reg_in["111"] = 0
            a=self.arr[1]
            b=self.arr[2]
            c=""
            d=""
            c=a//b
            d=a%b
            self.reg_in['000']=c
            self.reg_in['001']=d
            PC+=1
        elif(self.arr[0]=='rs'):         #imm in dec
            self.reg_in["111"] = 0
            a=""
            a=self.reg_in[self.arr[1]]         
            b=self.arr[2]
            a=a>>b
            self.reg_in[self.arr[1]]=a
            PC+=1
        elif(self.arr[0]=='ls'):          #imm in dec
            self.reg_in["111"] = 0
            a=""
            a=self.reg_in[self.arr[1]]         
            b=self.arr[2]
            a=a<<b
            self.reg_in[self.arr[1]]=a
            PC+=1
        elif(self.arr[0]=='xor'):
            self.reg_in["111"] = 0
            a=self.arr[1]
            b=self.arr[2]
            c=""
            c=a^b
            self.reg_in[self.arr[3]]=c 
            PC+=1
        elif(self.arr[0]=='or'):
            self.reg_in["111"] = 0
            a=self.arr[1]
            b=self.arr[2]
            c=""
            c=a|b
            self.reg_in[self.arr[3]]=c 
            PC+=1
        elif(self.arr[0]=='and'):
            self.reg_in["111"] = 0
            a=self.arr[1]
            b=self.arr[2]
            c=""
            c=a&b
            self.reg_in[self.arr[3]]=c 
            PC+=1  
        elif(self.arr[0]=='not'):
            self.reg_in["111"] = 0
            a=self.arr[1]
            # print(a)
            c="".join(["1" if i == "0" else "0" for i in self.dectobin(a)])
            self.reg_in[self.arr[2]]= self.bin2dec(c)
            PC+=1
        elif(self.arr[0]=='cmp'):
            a=self.arr[1]
            b=self.reg_in[self.arr[2]]
            # print(a,b,PC)
            if(a>b):
                self.reg_in['111'] = 2
                PC+=1
            elif(a<b):
                self.reg_in['111'] = 4
                PC+=1           
            elif(a==b):
                self.reg_in['111'] = 1
                PC+=1

        elif(self.arr[0]=='jmp'):
            pcnew=int(self.arr[1])
            PC=pcnew
            self.reg_in["111"] = 0
        elif(self.arr[0]=='jlt'):
            pcnew=int(self.arr[1])
            # print("HELE")
            if(self.reg_in['111'] == 4):
                PC=pcnew
            else:
                PC=PC+1
            self.reg_in["111"] = 0
        elif(self.arr[0]=='jgt'):
            pcnew=int(self.arr[1])
            if(self.reg_in['111'] == 2):
                PC=pcnew
            else:
                PC=PC+1
            self.reg_in["111"] = 0
        elif(self.arr[0]=='je'):
            pcnew=int(self.arr[1])
            if(self.reg_in['111'] == 1):
                PC=pcnew
            else:
                PC=PC+1            
            self.reg_in["111"] = 0
        elif(self.arr[0]=='hlt'):
            # self.reg_in["111"] = 0
            self.halted=1       
        return PC                   