import os
fol_name="D:\\t"
for item in os.listdir("D:\\t"):
    if os.path.isfile(os.path.join(fol_name,item)):
        print("file:",item)
    else:
        print("folder:",item)
