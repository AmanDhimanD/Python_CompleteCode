try:
    x=int(input())
    d=1/x
except Exception as e:
    print(e)
    exit()
#finally excuted after try and except print
finally:
    print(f"From the finally2!!!")


print("Print only if there are no exception and Finally print after all error")