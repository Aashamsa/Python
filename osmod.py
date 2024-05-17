import os
path = "C:\\Users\\user\\Pictures\\Camera Roll"
files = os.listdir(path)
i = 1
for x in files:
    if x.endswith(".jpg"):
        os.rename(f"{path}\\{x}",f"{path}\\{i}")
        i += 1
    print(x)