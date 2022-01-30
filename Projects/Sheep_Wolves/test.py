l = [["ch", '', ''],['salvi'], ['e', '', 'e', 'se']]
for a in l:
    if(a[len(a)-1]=="salvi"):
        a.pop()
for f in range(len(l)):
    print(f)
print(l)
print([var for var in l if var])