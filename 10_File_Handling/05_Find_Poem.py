f=open('poem.txt')
t=f.read()
if 'Twinkle' or 'twinkle' in t:
    print("Yes,Present.")
else:
    print("Not,Present")
f.close()