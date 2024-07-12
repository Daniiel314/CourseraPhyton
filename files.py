# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
av = 0
count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    av += float(line[line.find('0'):])
    count+=1
print("Average spam confidence:",av/count)
