from collections import Counter
import re
cnt = Counter()

for word in ['red','blue','red','green','blue','blue']:
	cnt[word] += 1

print cnt
print type(cnt)
print cnt.most_common(3)


words = re.findall(r'\d{5,}', open('hamlet.txt').read().lower())

print words
#print Counter(words).most_common(10)


testre = re.findall(r'^thi', 'this this88 , \nthin 99, 0 is a test')
#print testre