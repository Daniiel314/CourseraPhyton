import json
import urllib.request

url = input('Enter location: ')
if len(url) < 1 : 
    url = 'http://py4e-data.dr-chuck.net/comments_2053434.json'

print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved',len(data),'characters')
info = json.loads(data)
print('User count:', len(info))
nums = list()
counts = info['comments']
nums = list()
for count in counts:
    nums.append(int(count['count']))
print('Count:', len(nums))
print('Sum:', sum(nums))