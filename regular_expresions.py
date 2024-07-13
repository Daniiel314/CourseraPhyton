import re
fname = input("Enter file:")
if len(fname) < 1:
    fname = "regex_sum_2053429.txt"
lines = open(fname)
count = 0
for ln in lines:
    values = re.findall('[0-9]+', ln)
    for value in values:
        count += int(value)
print(count)