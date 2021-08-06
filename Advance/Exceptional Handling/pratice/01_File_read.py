def readFile(filename):
    try:
        with open(filename,"r") as f:
            print(f.read())
    except FileNotFoundError:
        print(f"File {filename} is not Found in this Directory.")


readFile("01_i.txt")
readFile("01_ii.txt")
readFile("01_iii.txt")


# ---------------------------------------
# output:-  1st time (Before delete File)

# first File
# Second File
# Thrid File


# output:-  1st time (After delete File)
# first File
# Second File
# File 01_iii.txt is not Found in this Directory.