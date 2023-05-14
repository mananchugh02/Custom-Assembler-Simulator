def getBin8Bits(x,type):
    binaryint = format(x, 'b')
    ac_bin_int = binaryint.zfill(8)
    return ac_bin_int
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
    result+=j
    return result
def float2bin(float):
    j=""
    n=1
    while float!=1:
        x=int(float)
        float=float-x
        k=int(float*2)
        float=float*2
        k=str(k)
        j=j+k
    j=str(j)
    return j
def final(n):
    flag=0
    exp_final=""
    mantissa_final=""
    int_part=int(n)
    float_part=n-int_part
    bias=0
    if(float_part==0):
        float_bin='0'
    else:
        float_bin=float2bin(float_part)
    int_bin=dectobin(int_part)
    n=0
    for i in range(len(int_bin)):
        if int_bin[i]=='1':
            break
        n+=1
    int_bin1=int_bin[n:len(int_bin)+1]
    float_extra=int_bin[1:len(int_bin1)+1]
    exp=len(int_bin1)-1
    exp_dec=bias+exp
    exp_bin=dectobin(exp_dec)
    mantissa=float_extra+float_bin
    exp_final+="0"*(3-len(exp_bin))
    exp_final+=exp_bin
    if(len(exp_final)>3):
        flag=1
    mantissa_final=mantissa_final.rstrip('0')
    mantissa_final=mantissa+"0"*(5-len(mantissa))
    if(len(mantissa_final)>5):
        flag=1
    finalotpt=exp_final+mantissa_final
    return finalotpt,flag

