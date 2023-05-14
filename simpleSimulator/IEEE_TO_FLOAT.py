def bin2dec(formatted_num):
    n = len(formatted_num)
    s = 0
    formatted_num = formatted_num[::-1]
    for i in range(n):
        s += (int(formatted_num[i])*(2**i))
    return s
def bin2float(bin):
    sum=0
    for i in range(1,len(bin)):
        sum=sum+(int(bin[i])*((1/2)**i))
    return sum
def final(inp):
    exp=inp[0:3]
    mantissa=inp[3:8]
    power=bin2dec(exp)
    num=""
    num=num+'1'
    num=num+mantissa
    num=num+('0'*(power-len(mantissa)))
    int_part=num[0:power+1]
    int_part=bin2dec(int_part)
    float_part=num[power:len(num)]    
    float_part=bin2float(float_part)
    result=int_part+float_part
    return result
