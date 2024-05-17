import os
def png(self,path):
    i = 1
    files = os.listdir(path)
    for x in files:
        if x.endswith(".png"):
            try:
                os.rename(f"{path}\\{x}",f"{path}\\{i}.png")
            except:
                os.rename(f"{path}\\{x}",f"{path}\\{i}.png")    
                i += 1

png("c:\\Users\\user\\Desktop\\Python","c:\\Users\\user\\Desktop\\Python\\image.png")