class OutputHandler:
    def __init__(self) -> None:
        pass
    def write(self,filename,data):
        f=open(filename+".txt",'a')
        for i in range(len(data)):
            for j in range(16):
                f.write(data[i][j])
            f.write("\n")
            