import os

for dirpath, dirnames, filenames in os.walk("./"):
    fpath = dirpath#.replace("ans",'')
    fpath = fpath and fpath + os.sep or ''
    for filename in filenames:
        if filename.find(" ") > 0:
            print("space!"+filename)
