import os
f = "1.txt"
ch = os.path.splitext(f)[0]
os.rename(f,ch+'.pdf')






