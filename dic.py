fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"
fh = open(fname)


counts = dict()
for line in fh:
    if 'From' in line and '2008' in line:
        email = line.split()[1]
        counts[email] = counts.get(email,0) + 1

count_max = 0
email_max = None

for email, count in counts.items():
    if count_max < count:
        count_max = count
        email_max = email

print(email_max, count_max)