def getBin8Bits(x,type):
    binaryint = format(x, 'b')
    ac_bin_int = binaryint.zfill(8)
    return ac_bin_int