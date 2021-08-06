try:
    x=int(input())
    d=1/x
except Exception as e:
    print(e)
#else print iff try run properly only
else:
    print(f"Done !!! 1/{x}")