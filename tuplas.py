name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

counts = dict()
for ln in handle:
    if 'From' in ln and '2008' in ln:
        hr = ln.split()[5][:2]
        counts[hr] = counts.get(hr,0) + 1
temp = list()
for hr, k in counts.items():
    temp.append((hr,k))
temp.sort()
for h, n in temp:
    print(h, n)