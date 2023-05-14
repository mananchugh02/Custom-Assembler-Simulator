from sys import stdin

def get_raw_file (filename,asm):
    lines =[]
    lineNumber = 0
    foundHalt =0
    
    for line in stdin:
        lineNumber+=1
        line = line.strip()
        line = line.split(";")[0]
        line = line.replace(","," ")
        line = line.split()
        if "hlt" in  line:
            foundHalt += 1
        # line = line.split()
        if line != [''] and line != []:
            line.append(lineNumber)
            lines.append(line)

    if (foundHalt==0):
       asm.errorHandler.handle(8,"NA")
    #    asm.errorHandler.errorState = 1
    elif (foundHalt >1):
       asm.errorHandler.handle(10,"NA")
    #    asm.errorHandler.errorState = 1
    elif (lines[-1][-2] != "hlt"):
       asm.errorHandler.handle(9,"NA")
    #    asm.errorHandler.errorState = 1 
#    
    return lines
