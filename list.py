fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    ls = line.split()
    for p in ls:
        if p not in lst:
            lst.append(p)
lst.sort()
print(lst)
